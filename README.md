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



-  PU-GCN (raw)
    ```shell
    python main.py --phase train --model pugcn --upsampler nodeshuffle --k 20 
    ```
   
-  PU-GCN (ProEdgeShuffle)
    ```shell
    python main.py --phase train --model pugcn --upsampler pronodeshuffle --k 20 
    ```

-  PU-Net (raw)
    ```
    python main.py --phase train --model punet --upsampler original  
    ```
   
-  PU-Net (ProEdgeShuffle)
    ```shell
    python main.py --phase train --model punet --upsampler pronodeshuffle --k 20 
    ```

-  MPU (raw)
    ```
    python main.py --phase train --model mpu --upsampler duplicate 
    ```

-  MPU (ProEdgeShuffle)
    ```shell
    python main.py --phase train --model mpu --upsampler pronodeshuffle --k 20 
    ```

-  PU-GAN (raw)
    ```
    python main.py --phase train --model pugan --more_up 2 
    ```
   
-  PU-GAN (ProEdgeShuffle)
    ```shell
    python main.py --phase train --model pugan --upsampler pronodeshuffle --k 20 
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


