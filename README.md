# E2E BRT Tester

Extensible Python end-to-end test runner for **BeRTA Renderer** and **BRT**.

The tester launches BeRTA Renderer, establishes a real OSC connection, keeps a live test session open, and executes perceptual or analytical tests declared in `test_registry.py`.

## Prerequisites

Before running the tester, make sure that the following components are available:

- Python 3.10 or later.
- BeRTA Renderer v3.13.0 or later.
- BRT v3.0.7 or later.
- A valid BeRTA Renderer settings file for each declared test.
- Python dependencies installed from `requirements.txt`.

BeRTA Renderer v3.13.0 or later is required because the analytical impulse-response tests use the `/recordIR` OSC command.

The current tests are intended to be valid for BRT v3.0.7 and later.

## Current features

Implemented functionality includes:

- Console application title and hierarchical menus.
- Internal `TestDefinition` model.
- Test filtering by type: analytical or perceptual.
- Navigation path shown at the top of each menu, for example:

```text
Main Menu / Analytical tests / Test 1
```

- Cross-platform BeRTA Renderer launcher.
- BeRTA process launched from its own installation directory.
- On Windows, BeRTA is launched in a separate console window.
- Settings file selection from `Settingsfiles/`.
- OSC startup verification using `/control/connect`, `/control/ping`, and `/control/version`.
- Robust OSC startup retry loop:
  - the tester retries `/control/connect` with a configurable wait time and maximum number of attempts;
  - only after BeRTA confirms the connection does the tester send `/control/ping` and `/control/version`.
- Live `TestSession` kept open after BeRTA is verified.
- Session actions for ping, version query, and test execution.
- BeRTA Renderer is closed when leaving the test session with either:
  - `[9] Disconnect and return to test menu`, or
  - `[0] Disconnect and exit`.
- Perceptual localization test.
- Analytical impulse-response test using `/recordIR` and WAV comparison.
- Unit tests for the audio comparison logic.

## Install dependencies

From the project root:

```bash
pip install -r requirements.txt
```

On Windows, if you are using the local virtual environment created for the project:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Or, on Windows with the local virtual environment:

```powershell
.\.venv\Scripts\python.exe main.py
```

## Menu structure

When the application starts, the main menu is:

```text
Path: Main Menu

[1] Analytical tests
[2] Perceptual tests
[0] Exit
```

Selecting one of the test categories shows only the tests of that type, as declared in `test_registry.py`.

Example:

```text
Path: Main Menu / Analytical tests

Available tests:

[1] Analytical impulse response test (analytical)
    Generates a stereo impulse response with BeRTA and compares it against a stereo WAV reference using strict NRMSE per channel.
    Settings file: Settingsfiles/analytical_test1.json

[9] Back to main menu
[0] Exit
```

After selecting a test, BeRTA Renderer is launched and verified through OSC. Once the connection is ready, the live session menu is shown:

```text
Path: Main Menu / Analytical tests / Test 1

Test session actions:
[1] Show session status
[2] Send /control/ping
[3] Request /control/version
[4] Run test actions
[9] Disconnect and return to test menu
[0] Disconnect and exit
```

## Project layout

```text
.
├── main.py
├── requirements.txt
├── pytest.ini
├── berta_tester/
│   ├── __init__.py
│   ├── analytical_tests.py
│   ├── app_config.py
│   ├── audio_io.py
│   ├── audio_metrics.py
│   ├── berta_launcher.py
│   ├── cli.py
│   ├── osc_client.py
│   ├── paths.py
│   ├── perceptual_tests.py
│   ├── test_actions.py
│   ├── test_definition.py
│   ├── test_registry.py
│   └── test_runner.py
├── Settingsfiles/
│   ├── analytical_test1.json
│   └── ...
├── Referencefiles/
│   ├── analytical_test1_ir_reference.wav
│   └── ...
├── Results/
│   └── analytical_ir/
├── Logs/
└── tests/
    └── test_audio_metrics.py
```

## BeRTA executable defaults

Windows:

```text
C:\Program Files\University of Malaga\BeRTA-Renderer App\BeRTA-Renderer.exe
```

macOS:

```text
/Applications/BeRTA-Renderer.app/Contents/MacOS/BeRTA-Renderer
```

You can override the executable path with an environment variable:

```bash
BERTA_RENDERER_EXECUTABLE="/custom/path/to/BeRTA-Renderer" python main.py
```

On Windows PowerShell:

```powershell
$env:BERTA_RENDERER_EXECUTABLE="C:\custom\path\BeRTA-Renderer.exe"
python main.py
```

## OSC defaults

The tester assumes these OSC endpoints by default:

```text
BeRTA receives OSC at: 127.0.0.1:10017
Tester receives replies at: 127.0.0.1:10011
Version/ping timeout after connection: 15 seconds
Connect retry wait: 2 seconds
Connect max attempts: 3
```

Override them with environment variables:

```bash
BERTA_OSC_IP="127.0.0.1"
BERTA_OSC_PORT="10017"
TESTER_OSC_IP="127.0.0.1"
TESTER_OSC_PORT="10011"
BERTA_OSC_STARTUP_TIMEOUT="15"
BERTA_OSC_CONNECT_RETRY_WAIT_SECONDS="2"
BERTA_OSC_CONNECT_MAX_ATTEMPTS="3"
python main.py
```

On Windows PowerShell:

```powershell
$env:BERTA_OSC_PORT="10017"
$env:TESTER_OSC_PORT="10011"
$env:BERTA_OSC_STARTUP_TIMEOUT="15"
$env:BERTA_OSC_CONNECT_RETRY_WAIT_SECONDS="2"
$env:BERTA_OSC_CONNECT_MAX_ATTEMPTS="3"
python main.py
```

## Test definitions

Tests are declared in:

```text
berta_tester/test_registry.py
```

Each test is represented by a `TestDefinition`.

The `id` is used only for menu selection. The test execution logic is selected using `test_type`:

```python
TestType.ANALYTICAL
TestType.PERCEPTUAL
```

This means that analytical and perceptual tests can be reordered freely in `test_registry.py`. The hierarchical menu will filter them automatically by type.

## Perceptual localization test

The perceptual localization test moves a source from the front position towards either the left or right ear.

The direction is randomly selected before the movement starts:

```text
front:      (1, 0, 0)
left ear:   (0, 1, 0)
right ear:  (0, -1, 0)
```

After the movement, the user is asked whether the source moved towards the left or right ear. The answer is compared with the actual random direction and the test reports PASS or FAIL.

## Analytical impulse-response test

The analytical impulse-response test verifies that a BeRTA configuration produces the expected binaural impulse response.

The test flow is:

```text
1. Verify that the OSC session with BeRTA is active.
2. Send /recordIR to BeRTA.
3. Wait for the real /control/actionResult response.
4. Check that BeRTA reports success.
5. Verify that the generated WAV file exists and is readable.
6. Open the generated stereo WAV and the stereo reference WAV.
7. Compare left channel against left channel.
8. Compare right channel against right channel.
9. Report PASS, FAIL, or ERROR.
```

The OSC command used is:

```text
/recordIR <filename> <type> <time> <period> <delay> <x> <y> <z>
```

For the current analytical tests, `type` is expected to be:

```text
wav
```

The expected OSC completion message is:

```text
/control/actionResult /recordIR <filename> <success> <description>
```

The tester does not continue to the file comparison until this real OSC response has been received.

### Main comparison metric

The main metric is strict per-channel NRMSE:

```text
NRMSE (%) = 100 * RMS(generated - reference) / RMS(reference)
```

It is calculated independently for:

```text
left generated  vs left reference
right generated vs right reference
```

A test passes only if both channels are below the configured margin:

```text
left_nrmse  < margin
right_nrmse < margin
```

The default margin is:

```text
1.0 %
```

The margin is configurable in the corresponding `TestDefinition`.

### Complementary diagnostics

The analytical test also reports:

- correlation per channel;
- peak absolute error per channel;
- RMS level per channel;
- level difference in dB per channel;
- detected temporal offset using cross-correlation;
- diagnostic NRMSE after alignment;
- optional channel-swap warning.

Temporal alignment is diagnostic only. The strict PASS/FAIL decision uses the original sample positions.

### WAV validation

Before comparing signals, the tester validates that:

- both files exist;
- both files can be opened;
- both files are valid WAV files;
- both files contain exactly two channels;
- both files have the same sample rate;
- samples can be converted to floating point;
- the signals have the same number of samples for strict comparison;
- silent reference channels are detected to avoid division by zero.

If the lengths are different, the strict comparison fails. A common-region diagnostic may still be shown, but it does not turn the result into PASS.

## Reference files and generated results

`Referencefiles/` contains the reference material used by the analytical tests. These files are part of the expected software behaviour and should be versioned in Git.

`Results/` contains files generated while running tests. These files should not normally be committed.

Recommended policy:

```text
Commit:
- berta_tester/
- tests/
- Settingsfiles/ reproducible test configurations
- Referencefiles/ reference WAV files
- requirements.txt
- README.md

Do not commit:
- .venv/
- Results/
- Logs/
- .env files
- local settings files with machine-specific absolute paths
```

## Running unit tests

```bash
pytest -q
```

The current unit tests cover the audio comparison and validation logic, including:

- identical files;
- gain changes;
- temporal shift detection;
- swapped channels;
- different lengths;
- silent reference channel;
- invalid mono WAV;
- sample-rate mismatch.

## Notes on Windows paths

For Windows, avoid very long output paths when possible. Some native audio libraries may fail to open valid WAV files if the absolute path is too long.

If needed, use shorter locations for generated and reference files, for example:

```text
C:\BERTA_TEST\Results\generated_test1_ir.wav
C:\BERTA_TEST\Reference\analytical_test1_ir_reference.wav
```

The tester includes additional fallback logic for reading WAV files from long paths, but using short paths is still recommended for robust E2E runs.

## Current limitations

- The analytical impulse-response test currently expects WAV output from `/recordIR`.
- MAT output is not implemented in the Python reader yet.
- The CLI is synchronous: all operations use timeouts, but the console is occupied while waiting for BeRTA or comparing audio files.
- The tester assumes that each test settings file fully defines a deterministic BeRTA configuration.
