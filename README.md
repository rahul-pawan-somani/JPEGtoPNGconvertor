# ParallelImageProcessor

This Python script leverages concurrent processing to efficiently convert a batch of images in a specified folder to the PNG format. It utilizes the Pillow (PIL) library for image manipulation and the `concurrent.futures.ThreadPoolExecutor` for parallel execution.

## Usage

To utilize the script, execute it from the command line with the following format:

```bash
python ParallelImageProcessor.py <image_folder>
```

- `<image_folder>`: The path to the folder containing the images to be processed.

### Example:

```bash
python ParallelImageProcessor.py /path/to/images
```

## Dependencies

Ensure that you have the Pillow library installed:

```bash
pip install Pillow
```

## Features

- **Parallel Processing:**
  - Images in the specified folder are processed concurrently using a thread pool, enhancing the overall speed of image conversion.

- **Error Handling:**
  - The script includes error handling to manage potential issues, such as missing image folders or errors during image processing.

## Notes

- Processed images are saved in the same directory as their corresponding input images with the '.png' extension.

- It is recommended to provide a valid image folder path to avoid errors.

## License

This script is provided under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this script according to the terms of the license. If you encounter any issues or have suggestions for improvement, please feel free to contribute or open an issue. Happy image processing!
