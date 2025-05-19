


# Airtest Game Testing Automation

Hello there! This is a simple script to demonstrate the capabilities of airtest in the context of game testing. This is connected via the airtest api and demonstrate some of the common techniques used, enjoy!


## Overview

This repository contains a working example of using Airtest to automate UI interactions in Windows applications, specifically demonstrating:
- Automated text input
- Image recognition for UI elements
- Touch/mouse interactions
- Screenshot capture for verification

## Prerequisites

- Windows operating system
- Python 3.x
- Required Python packages:
  ```bash
  pip install airtest
  pip install six pillow opencv-python pywinauto ffmpeg-python jinja2
  ```

## Project Structure

```
airtest-gametesting/
├── README.md
├── airtest_script.py
├── homebutton.png
└── searchbar.png
```

## Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/andiAtSIDE/airtest-gametesting.git
   cd airtest-gametesting
   ```

2. Install required dependencies:
   ```bash
   pip install airtest
   pip install six pillow opencv-python pywinauto ffmpeg-python jinja2
   ```

3. Prepare image files:
   - Capture and save `homebutton.png` - screenshot of the home button
   - Capture and save `searchbar.png` - screenshot of the search bar

## Usage

Run the automation script:
```bash
python airtest_script.py
```

The script will:
1. Connect to the Windows desktop
2. Open Notepad
3. Type "hello world!"
4. Click the home button
5. Click the search bar
6. Type "hello world!" again
7. Take a screenshot of the result

## Script Details

The main script (`airtest_script.py`) includes:
- Environment setup and device connection
- Debug logging
- Error handling
- Image recognition for UI elements
- Keyboard input simulation
- Screenshot capture

## Troubleshooting

Common issues and solutions:

1. **Dependency Errors**
   - Ensure all required packages are installed
   - Check Python version compatibility

2. **Image Recognition Issues**
   - Verify image files are clear and unique
   - Check image file paths
   - Adjust recognition threshold if needed

3. **Permission Issues**
   - Run as administrator if needed
   - Check file access permissions

4. **Application Launch Issues**
   - Verify application paths
   - Check if application is installed
   - Ensure application is accessible

## Best Practices

1. **Image Files**
   - Keep images in the same directory as the script
   - Use clear, unique images for recognition
   - Maintain consistent image quality

2. **Script Structure**
   - Include debug print statements
   - Use try-except blocks for error handling
   - Add appropriate sleep times between actions
   - Take screenshots at key points

3. **Documentation**
   - Document package versions
   - Note application-specific requirements
   - Include setup instructions
   - Document any special considerations

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Airtest Project Team
- OpenCV
- Python Community
