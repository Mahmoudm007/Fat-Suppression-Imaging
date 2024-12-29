import streamlit as st
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import tempfile
import os


def load_nifti(file):
    tmpfile_path = os.path.join(tempfile.gettempdir(), "tempfile.nii")

    with open(tmpfile_path, "wb") as tmpfile:
        tmpfile.write(file.read())  # Save the content of the uploaded file

    # Load the NIFTI data from the temporary file path
    img = nib.load(tmpfile_path)

    # Return the data
    return img.get_fdata()


def fat_water_separation(data_ip, data_op):
    water_component = (data_ip + data_op) / 2
    fat_component = (data_ip - data_op) / 2
    return fat_component, water_component


def main():
    st.title("Fat/Water Separation Viewer")

    file1 = st.file_uploader(
        "Upload the IP (In-Phase) NIFTI file", type=["nii", "nii.gz"]
    )
    file2 = st.file_uploader(
        "Upload the OP (Out-of-Phase) NIFTI file", type=["nii", "nii.gz"]
    )

    if file1 and file2:
        try:
            data1 = load_nifti(file1)
            data2 = load_nifti(file2)
            st.success("NIFTI files loaded successfully!")
        except Exception as e:
            st.error(f"Error loading NIFTI files: {e}")
            return

        if len(data1.shape) < 3 or len(data2.shape) < 3:
            st.error("The NIFTI files must be 3D data (at least width, height, depth).")
            return

        max_slices = min(data1.shape[2], data2.shape[2])
        slice_idx = st.slider("Select Slice", 0, max_slices - 1, max_slices // 2)

        fat, water = fat_water_separation(data1, data2)

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

        # Plot IP slice
        ax1.imshow(data1[:, :, slice_idx], cmap="gray", interpolation="nearest")
        ax1.set_title("IP")
        ax1.axis("off")

        # Plot OP slice
        ax2.imshow(data2[:, :, slice_idx], cmap="gray", interpolation="nearest")
        ax2.set_title("OP")
        ax2.axis("off")

        # Plot Water component
        ax3.imshow(water[:, :, slice_idx], cmap="gray", interpolation="nearest")
        ax3.set_title("Water")
        ax3.axis("off")

        # Plot Fat component
        ax4.imshow(fat[:, :, slice_idx], cmap="gray", interpolation="nearest")
        ax4.set_title("Fat")
        ax4.axis("off")

        # Adjust layout
        plt.tight_layout()

        # Display the plot
        st.pyplot(fig)


# Run the app
if __name__ == "__main__":
    main()
