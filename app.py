import cv2
import numpy as np
import streamlit as st
from PIL import Image


class ImageProcessingPipeline:
    """
    A class to handle image processing tasks.
    """

    def __init__(self):
        self.image = None
        self.gray_image = None
        self.blurred_image = None
        self.sobel_edges = None
        self.canny_edges = None

    @staticmethod
    def load_image(image_file):
        """
        Load an image from the uploaded file.

        :param image_file: The uploaded image file.
        :return: A NumPy array representing the loaded image.
        """
        img = Image.open(image_file)
        return np.array(img)  # Convert PIL image to OpenCV format

    @staticmethod
    def convert_to_grayscale(image):
        """
        Convert the input image to grayscale.

        :param image: The input image as a NumPy array.
        :return: A grayscale version of the input image.
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def apply_gaussian_blur(gray_image, kernel_size=(5, 5), sigma=0):
        """
        Apply Gaussian blur to the grayscale image.

        :param gray_image: The grayscale image as a NumPy array.
        :param kernel_size: The size of the Gaussian kernel. Default is (5, 5).
        :param sigma: Standard deviation in X and Y directions. Default is 0.
        :return: A blurred version of the input image.
        """
        return cv2.GaussianBlur(gray_image, kernel_size, sigma)

    @staticmethod
    def sobel_edge_detection(blurred_image):
        """
        Perform Sobel edge detection on the blurred image.

        :param blurred_image: The blurred image as a NumPy array.
        :return: An image with detected edges using Sobel method.
        """
        sobelx = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0)
        sobely = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1)
        abs_sobelx = np.absolute(sobelx)
        abs_sobely = np.absolute(sobely)
        gradmag = np.sqrt((sobelx**2 + sobely**2), dtype=np.float32)
        gradmag_normalized = cv2.normalize(
            gradmag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U
        )
        return gradmag_normalized

    @staticmethod
    def canny_edge_detection(blurred_image, threshold1=50, threshold2=150):
        """
        Perform Canny edge detection on the blurred image.

        :param blurred_image: The blurred image as a NumPy array.
        :param threshold1: First threshold for hysteresis procedure. Default is 50.
        :param threshold2: Second threshold for hysteresis procedure. Default is 150.
        :return: An image with detected edges using Canny method.
        """
        return cv2.Canny(blurred_image, threshold1, threshold2)

    @staticmethod
    def compute_histogram(gray_image):
        """
        Compute the histogram of a grayscale image.

        :param gray_image: The grayscale image as a NumPy array.
        :return: A list representing the frequency of each intensity value in the image.
        """
        hist = np.zeros(256, dtype=int)
        for i in range(gray_image.shape[0]):
            for j in range(gray_image.shape[1]):
                intensity = gray_image[i, j]
                hist[intensity] += 1
        return hist

    def display_histogram(self):
        """
        Display histogram of grayscale image using Streamlit.
        """
        hist = self.compute_histogram(self.gray_image)
        st.write("Grayscale Image")
        st.image(
            cv2.cvtColor(self.gray_image, cv2.COLOR_GRAY2RGB),
            caption="Original Grayscale Image",
            use_container_width=True,
        )
        st.caption("Grayscale Image Histogram")
        st.bar_chart(hist)

    def show_instructions(self):
        """
        Display instructions to the user.
        """
        st.title("Computer Vision Pipeline with Streamlit")
        st.write("""
            ## What This Script Does:
            - **Load Image**: You can upload an image.
            - **Grayscale Conversion**: The image is converted to grayscale.
            - **Gaussian Blur**: A Gaussian blur is applied to the grayscale image.
            - **Sobel Edge Detection**: Sobel edge detection is performed on the blurred image.
            - **Canny Edge Detection**: Canny edge detection is performed on the blurred image.
            - **Histogram Computation and Display**: The histogram of the grayscale image is computed and displayed.
        """)

    def main(self):
        """
        Main method to handle the entire pipeline workflow.
        """
        self.show_instructions()
        st.title("Computer Vision Pipeline")

        uploaded_file = st.file_uploader(
            "Choose an image...", type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:
            self.image = ImageProcessingPipeline.load_image(uploaded_file)
            self.gray_image = ImageProcessingPipeline.convert_to_grayscale(
                self.image)
            self.blurred_image = ImageProcessingPipeline.apply_gaussian_blur(
                self.gray_image)

            self.sobel_edges = ImageProcessingPipeline.sobel_edge_detection(
                self.blurred_image)
            self.canny_edges = ImageProcessingPipeline.canny_edge_detection(
                self.blurred_image)

            st.title("Results")

            st.image(self.image, caption="Uploaded Image",
                     use_container_width=True)

            st.image(
                cv2.cvtColor(self.gray_image, cv2.COLOR_GRAY2RGB),
                caption="Grayscale Image",
                use_container_width=True,
            )

            st.image(
                self.blurred_image, caption="Blurred Image", use_container_width=True
            )

            st.image(self.sobel_edges, caption="Sobel Edges",
                     use_container_width=True)

            st.image(self.canny_edges, caption="Canny Edges",
                     use_container_width=True)

            self.display_histogram()


# Main execution block
if __name__ == "__main__":
    app = ImageProcessingPipeline()
    app.main()
