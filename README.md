### Preparation

1. Clone the repository:

   ```shell
   https://github.com/zyh16143998882/ProEdgeShuffle.git
   cd ProEdgeShuffle
   ```
   
2. install the environment. Please refer [PU-GCN](https://github.com/guochengqian/PU-GCN)

3. Download PU1K dataset from [Google Drive](https://drive.google.com/file/d/1oTAx34YNbL6GDwHYL2qqvjmYtTVWcELg/view?usp=sharing)  
    Link the data to `./data`:

    ```bash
    mkdir data
    ln -s /path/to/PU1K ./data/
    ```
4. Optional. The original meshes of PU1K dataset is avaialble in [Goolge Drive](https://drive.google.com/file/d/1tnMjJUeh1e27mCRSNmICwGCQDl20mFae/view?usp=sharing)
    
### Train

Train models. Our pretrained models are available [Google Drive](https://drive.google.com/file/d/1vusBIw7sd69gnyaeoWMiGaPHfkyHM5Qb/view?usp=sharing)

-  PU-GCN
    ```shell
    python main.py --phase train --model pugcn --upsampler nodeshuffle --k 20 
    ```

-  PU-Net
    ```
    python main.py --phase train --model punet --upsampler original  
    ```

-  MPU
    ```
    python main.py --phase train --model mpu --upsampler duplicate 
    ```

-  PU-GAN
    ```
    python main.py --phase train --model pugan --more_up 2 
    ```



### Evaluation

1. Test on PU1K dataset
   ```bash
   bash test_pu1k_allmodels.sh # please modify this script and `test_pu1k.sh` if needed
   ```

5. Test on real-scanned dataset

    ```bash
    bash test_realscan_allmodels.sh
    ```

6. Visualization. 
    check below. You have to modify the path inside. 
    
    ```bash
    python vis_benchmark.py
    ```



​    
### Acknowledgement
This repo is heavily built on [PU-GCN code](https://github.com/guochengqian/PU-GCN).


