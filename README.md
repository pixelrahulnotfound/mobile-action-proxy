# Mobile Action Proxy

Mobile Action Proxy is a lightweight tool for capturing network traffic generated during AI-driven mobile application testing.
The project combines MobileRun for autonomous app interaction with mitmproxy for HTTP interception.While the AI performs user-defined tasks inside an Android application, every outgoing request is captured and organized according to the action being executed.This makes it easy to inspect API behavior,understand application workflows, and analyze network traffic during automated testing.

## Features
- AI-powered mobile application interaction
- Automatic HTTP request interception using mitmproxy
- Action-based organization of captured traffic
- JSON output for easy analysis
- Simple architecture that is easy to extend

## Project Structure

```
mobile-action-proxy/
│
├── output/
│   └── sessions/
│       └── run_001.json
│
├── proxy/
│   ├── actions.py
│   ├── capture.py
│   └── state.json
│
├── main.py
└── README.md
```

## How It Works
1. Start the program.
2. Enter the Android device ID.
3. Specify the target application.
4. Describe the actions you want the AI to perform.
5. MobileRun executes the task on the device.
6. mitmproxy captures every HTTP request generated during execution.
7. Captured requests are grouped by action and saved as JSON.

## Requirements
- Python 3.10 or later
- MobileRun SDK
- mitmproxy
- Android device
- MobileRun Cloud API key

## Installation

Clone the repository.

```bash
git clone https://github.com/pixelrahulnotfound/mobile-action-proxy
cd mobile-action-proxy
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Set your API key.

```bash
export MOBILERUN_CLOUD_API_KEY=<your_api_key>
```

## Usage

Run the application.

```bash
python main.py
```

You will be prompted for:
- Device ID
- Target application
- Testing task

Example task:
```
Open Instagram.
Navigate to the profile page.
Edit the bio.
Like five posts.
```

Captured requests are written to:
```
output/sessions/run_001.json
```

## Example Output

```json
{
  "OPEN_PROFILE": [
    {
      "method": "POST",
      "url": "...",
      "headers": {},
      "body": "..."
    }
  ]
}
```

## Use Cases

- Mobile application security testing
- API traffic analysis
- Bug bounty reconnaissance
- Reverse engineering mobile applications
- Automated workflow analysis

## Future Work

- Capture HTTP responses
- Support multiple testing sessions
- Export HAR files
- Generate API summaries
- Add a simple web dashboard

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2026 Rahul Kumar , Prashant Kumar , Pratyush Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```