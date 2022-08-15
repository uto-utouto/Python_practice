OpenCV ObjDetect Module Face Recognition (SFace) Sample
=======================================================
 
* 1. Generate Aligned Faces  
  ```
  python generate_aligned_faces.py image.jpg
  ```

  * Input  
    ![input](https://user-images.githubusercontent.com/816705/136777535-36d6bce1-91bf-446c-9377-645cc60b9c65.jpg)  

  * Outputs  
    ![face001](https://user-images.githubusercontent.com/816705/136901725-0c1e6002-ffa0-4a7a-bf73-a4933cf48e82.jpg)  
    ![face002](https://user-images.githubusercontent.com/816705/136901726-0b35c2bb-abf4-47a2-9119-6e7834dfd3a1.jpg)  
    
* 2. Generate Feature Dictionary  
  ```
  python generate_feature_dictionary.py face001.jpg
  python generate_feature_dictionary.py face002.jpg
  ```

  * Inputs  
    ![face001](https://user-images.githubusercontent.com/816705/136901725-0c1e6002-ffa0-4a7a-bf73-a4933cf48e82.jpg)  
    ![face002](https://user-images.githubusercontent.com/816705/136901726-0b35c2bb-abf4-47a2-9119-6e7834dfd3a1.jpg)  
    
  * Outputs  
    * face001.npy  
    * face002.npy  

* Face Recognizer  
  * Input  
    ![input](https://user-images.githubusercontent.com/816705/136777535-36d6bce1-91bf-446c-9377-645cc60b9c65.jpg)  

  * Output (NOTE: label is file name of dictionary)  
    ![output](https://user-images.githubusercontent.com/816705/136903110-7ced649d-53f4-4436-8060-096f547518f5.jpg)  

Download
--------
[yunet.onnx](https://github.com/ShiqiYu/libfacedetection.train/blob/master/tasks/task1/onnx/yunet.onnx)  
[face_recognizer_fast.onnx](https://drive.google.com/file/d/1ClK9WiB492c5OZFKveF3XiHCejoOxINW/view?usp=sharing)  

Reference
---------
[DNN-based Face Detection And Recognition | OpenCV Tutorials](https://docs.opencv.org/4.5.4/d0/dd4/tutorial_dnn_face.html)  
[cv::FaceDetectorYN Class Reference | OpenCV Online Documentation](https://docs.opencv.org/4.5.4/df/d20/classcv_1_1FaceDetectorYN.html)  
[cv::FaceRecognizerSF Class Reference | OpenCV Online Documentation](https://docs.opencv.org/4.5.4/da/d09/classcv_1_1FaceRecognizerSF.html)   