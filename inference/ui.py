import streamlit as st
from engine import inference
import os


def ui():
    st.markdown("# Brain MRI FLAIR Segmentation")
    st.markdown(
        "***A MobileNet v3 based segmentation project to perform instance segmentation \
        on FLAIR (Fluid-Attenuated Inversion Recovery) abnormality in brain MRI images. This model is trained using \
        [Brain MRI segmentation](https://www.kaggle.com/mateuszbuda/lgg-mri-segmentation) from kaggle. \
        This is a complete MLOPS project.***"
    )
    st.markdown(
        "## [Code on GitHub](https://github.dev/swathisekar1411/Brain-MRI-FLAIR-Segmentation)"
    )

    st.markdown("# Examples")
    st.markdown(
        "***The green outlined area is the predicted abnormality and the red outlined area \
        is the ground truth. The model performs great while also having less memory foot print.***"
    )
    st.image("images/predictions.png", width=800, channels="RGB")

    st.markdown("# Try it out:")
    st.markdown("##### ***Here's an example mri image, download this and upload it onto the file uploader***")
    st.image("images/sample-1.png", width=300, channels="RGB")
    uploaded_file = st.file_uploader(
        "Upload an MRI slice", type=["tif", "tiff", "png", "jpeg", "jpg"]
    )

    if uploaded_file is not None:
        inference(img_path=uploaded_file)
        st.image("inference/result.png", width=500, channels="RGB", caption="predicted mask")
    st.markdown("")
    st.markdown(
        """# Connect with me
  [<img height="30" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />][github]
  [<img height="30" src="https://img.shields.io/badge/linkedin-blue.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />][LinkedIn]
  
  [github]: https://github.com/swathisekar1411
  [linkedin]: https://www.linkedin.com/in/swathi-sekar-/""",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    ui()
