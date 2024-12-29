# Fat/Water Separation Viewer

This Streamlit app allows you to upload NIFTI files (In-Phase and Out-of-Phase), perform fat/water separation, and visualize the results in interactive slices.

## Installation

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

- Windows:

```bash
.\venv\Scripts\activate
```

- macOS/Linux:

```bash
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run main.py
```

## Usage

- Upload the IP (In-Phase) and OP (Out-of-Phase) NIFTI files.
- Use the slider to navigate through the slices.
- View the fat/water separation results.
