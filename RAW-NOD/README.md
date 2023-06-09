# RAW-NOD (Night Object Detection) Dataset
_GenISP: Neural ISP for Low-Light Machine Cognition_, CPRR NTIRE Workshop 2022

[Igor Morawski](https://igor-morawski.github.io/), Yu-An Chen, Yu-Sheng Lin, Shusil Dangi, Kai He, [Winston H. Hsu](https://winstonhsu.info/)

## Please download the dataset using the [link](https://docs.google.com/forms/d/1aIKTV6026daYFRtje7zcx4LeDz68AOcpWIH7XxNCICY/).

### Dataset Introduction
We present a high-quality large-scale dataset for low-light object detection using raw sensor data of outdoor images targeting low-light object detection. The dataset contains more than 7K images and 46K annotated objects (with bounding boxes) that belong to classes: _person_, _bicycle_, and _car_. The photos were taken on the streets at evening hours, and thus all images present low-light conditions to a varying degree of severity. We used two DSLR cameras to capture the scenes: Sony RX100 VII and Nikon D750, and throughout the paper, we refer to the sets collected by these cameras as Sony and Nikon (data)set. We show the statistics of our dataset in the table below.

| Dataset | Camera | #classes | #annotated images | #instances | #unannotated images |
|--- |--- |--- |--- |--- |--- |
| Sony | Sony RX100 VII | 3 | 3.2k | 18.7k | 0.9k |
| Nikon | Nikon D750 | 3 | 4.0k | 28.0k | 0 |
| NOD (in total) | Sony+Nikon | 3 | 7.2k | 46.7k | 0.9k |

### Citation
If you find our dataset useful in your research or publication, please cite our work:
```
@inproceedings{morawski2022genisp,
  title={GenISP: Neural ISP for Low-Light Machine Cognition},
  author={Morawski, Igor and Chen, Yu-An and Lin, Yu-Sheng and Dangi, Shusil and He, Kai and Hsu, Winston H},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={630--639},
  year={2022}
}
```

### Contact
Igor Morawski: [e-mail](mailto:igor@cmlab.csie.ntu.edu.tw), [LinkedIn](https://www.linkedin.com/in/igor-morawski/).

### Acknowledgement
This work was supported in part by the Ministry of Science and Technology, Taiwan, under Grant MOST 110-2634-F-002-051 and Qualcomm Technologies, Inc. We are grateful to the National Center for
High-performance Computing.