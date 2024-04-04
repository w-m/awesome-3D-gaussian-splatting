## Table of Contents:
- [Autonomous Driving](#autonomous-driving)
- [Avatars](#avatars)
- [Classic work](#classic-work)
- [Compression](#compression)
- [Diffusion](#diffusion)
- [Dynamics and Deformation](#dynamics-and-deformation)
- [Editing](#editing)
- [Language Embedding](#language-embedding)
- [Large-Scale](#large-scale)
- [Mesh Extraction and Physics](#mesh-extraction-and-physics)
- [Misc](#misc)
- [Navigation](#navigation)
- [Poses](#poses)
- [Regularization and Optimization](#regularization-and-optimization)
- [Rendering](#rendering)
- [Reviews](#reviews)
- [SLAM](#slam)
- [Seminal Paper introducing 3D Gaussian Splatting](#seminal-paper-introducing-3d-gaussian-splatting)
- [Sparse](#sparse)

___
<br>

<a name="autonomous-driving"></a>
# Autonomous Driving
- <a name="yunzhi20240street"></a>Yunzhi Yan, Haotong Lin, Chenxu Zhou, Weijie Wang, Haiyang Sun, Kun Zhan, Xianpeng Lang, Xiaowei Zhou, Sida Peng,  
  *[Street Gaussians for Modeling Dynamic Urban Scenes](https://arxiv.org/pdf/2401.01339.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.01339.pdf), [Project Page](https://zju3dv.github.io/street_gaussians/), [Code](https://github.com/zju3dv/street_gaussians)
- <a name="xiaoyu20230drivinggaussian"></a>Xiaoyu Zhou, Zhiwei Lin, Xiaojun Shan, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang,  
  *[DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes](https://arxiv.org/pdf/2312.07920.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.07920.pdf), [Project Page](https://pkuvdig.github.io/DrivingGaussian/)

<a name="avatars"></a>
# Avatars
- <a name="mengtian20240gaussianbody"></a>Mengtian Li, Shengxiang Yao, Zhifeng Xie, Keyu Chen, Yu-Gang Jiang,  
  *[GaussianBody: Clothed Human Reconstruction via 3d Gaussian Splatting](https://arxiv.org/pdf/2401.09720.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.09720.pdf)
- <a name="zhongyuan20240psavatar"></a>Zhongyuan Zhao, Zhenyu Bao, Qing Li, Guoping Qiu, Kanglin Liu,  
  *[PSAvatar: A Point-based Morphable Shape Model for Real-Time Head Avatar Creation with 3D Gaussian Splatting](https://arxiv.org/pdf/2401.12900.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.12900.pdf)
- <a name="alfredo20240rig3dgs"></a>Alfredo Rivero, ShahRukh Athar, Zhixin Shu, Dimitris Samaras,  
  *[Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos](https://arxiv.org/pdf/2402.03723.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.03723.pdf), [Project Page](http://shahrukhathar.github.io/2024/02/05/Rig3DGS.html)
- <a name="zhenglin20240headstudio"></a>Zhenglin Zhou, Fan Ma, Hehe Fan, Yi Yang,  
  *[HeadStudio: Text to Animatable Head Avatars with 3D Gaussian Splatting](https://arxiv.org/pdf/2402.06149.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.06149.pdf), [Project Page](https://zhenglinzhou.github.io/HeadStudio-ProjectPage/), [Code](https://github.com/ZhenglinZhou/HeadStudio/)
- <a name="georgii20240implicitdeepfake"></a>Georgii Stanishevskii, Jakub Steczkiewicz, Tomasz Szczepanik, Sławomir Tadeja, Jacek Tabor, Przemysław Spurek,  
  *[ImplicitDeepfake: Plausible Face-Swapping through Implicit Deepfake Generation using NeRF and Gaussian Splatting](https://arxiv.org/pdf/2402.06390.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.06390.pdf), [Code](https://github.com/quereste/implicit-deepfake)
- <a name="haimin20240gaussianhair"></a>Haimin Luo, Min Ouyang, Zijun Zhao, Suyi Jiang, Longwen Zhang, Qixuan Zhang, Wei Yang, Lan Xu, Jingyi Yu,  
  *[GaussianHair: Hair Modeling and Rendering with Light-aware Gaussians](https://arxiv.org/pdf/2402.10483.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.10483.pdf)
- <a name="xinqi20240gva"></a>Xinqi Liu, Chenming Wu, Jialun Liu, Xing Liu, Jinbo Wu, Chen Zhao, Haocheng Feng, Errui Ding, Jingdong Wang,  
  *[GVA: Reconstructing Vivid 3D Gaussian Avatars from Monocular Videos](https://arxiv.org/pdf/2402.16607.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.16607.pdf), [Project Page](https://3d-aigc.github.io/GEA/)
- <a name="zhijing20240splattingavatar"></a>Zhijing Shao, Zhaolong Wang, Zhuang Li, Duotun Wang, Xiangru Lin, Yu Zhang, Mingming Fan, Zeyu Wang,  
  *[SplattingAvatar: Realistic Real-Time Human Avatars with Mesh-Embedded Gaussian Splatting](https://arxiv.org/pdf/2403.05087.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.05087.pdf), [Project Page](https://initialneil.github.io/SplattingAvatar), [Code](https://github.com/initialneil/SplattingAvatar), [Presentation](https://www.youtube.com/watch?v=IzC-fLvdntA)
- <a name="zhijing20240splatface"></a>Zhijing Shao, Zhaolong Wang, Zhuang Li, Duotun Wang, Xiangru Lin, Yu Zhang, Mingming Fan, Zeyu Wang,  
  *[SplatFace: Gaussian Splat Face Reconstruction Leveraging an Optimizable Surface](https://arxiv.org/pdf/2403.18784)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.18784)
- <a name="zhijing20240haha"></a>Zhijing Shao, Zhaolong Wang, Zhuang Li, Duotun Wang, Xiangru Lin, Yu Zhang, Mingming Fan, Zeyu Wang,  
  *[HAHA: Highly Articulated Gaussian Human Avatars with Textured Mesh Prior](https://arxiv.org/pdf/2404.01053)*,  
  2024, [PDF](https://arxiv.org/pdf/2404.01053)
- <a name="wojciech20230drivable"></a>Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero,  
  *[Drivable 3D Gaussian Avatars](https://arxiv.org/pdf/2311.08581.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.08581.pdf), [Project Page](https://zielon.github.io/d3ga/), [Presentation](https://youtu.be/C4IT1gnkaF0?si=zUJLm8adM68pVvR8)
- <a name="rohit20230splatarmor"></a>Rohit Jena, Ganesh Subramanian Iyer, Siddharth Choudhary, Brandon Smith, Pratik Chaudhari, James Gee,  
  *[SplatArmor: Articulated Gaussian splatting for animatable humans from monocular RGB videos](https://arxiv.org/pdf/2311.10812.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.10812.pdf), [Project Page](https://jenaroh.it/splatarmor/), [Code](https://github.com/rohitrango/splatarmor)
- <a name="zhe20230animatable"></a>Zhe Li, Zerong Zheng, Lizhen Wang, Yebin Liu,  
  *[Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling](https://arxiv.org/pdf/2311.16096.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16096.pdf), [Project Page](https://animatable-gaussians.github.io/), [Code](https://github.com/lizhe00/AnimatableGaussians)
- <a name="jiahui20230gart"></a>Jiahui Lei, Yufu Wang, Georgios Pavlakos, Lingjie Liu, Kostas Daniilidis,  
  *[GART: Gaussian Articulated Template Models](https://arxiv.org/pdf/2311.16099.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16099.pdf), [Project Page](https://www.cis.upenn.edu/~leijh/projects/gart/), [Code](https://github.com/JiahuiLei/GART), [Presentation](https://www.youtube.com/watch?v=-xYNtIlW4WY)
- <a name="arthur20230human"></a>Arthur Moreau, Jifei Song, Helisa Dhamo, Richard Shaw, Yiren Zhou, Eduardo Pérez-Pellitero,  
  *[Human Gaussian Splatting: Real-time Rendering of Animatable Avatars](https://arxiv.org/pdf/2311.17113.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17113.pdf)
- <a name="muhammed20230hugs"></a>Muhammed Kocabas, Jen-Hao Rick Chang, James Gabriel, Oncel Tuzel, Anurag Ranjan,  
  *[HUGS: Human Gaussian Splats](https://arxiv.org/pdf/2311.17910.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17910.pdf), [Project Page](https://machinelearning.apple.com/research/hugs), [Code](https://github.com/apple/ml-hugs)
- <a name="rameen20230gaussian"></a>Rameen Abdal, Wang Yifan, Zifan Shi, Yinghao Xu, Ryan Po, Zhengfei Kuang, Qifeng Chen, Dit-Yan Yeung, Gordon Wetzstein,  
  *[Gaussian Shell Maps for Efficient 3D Human Generation](https://arxiv.org/pdf/2311.17857)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17857), [Project Page](https://rameenabdal.github.io/GaussianShellMaps/), [Code](https://github.com/computational-imaging/GSM)
- <a name="jie20230gaussianhead"></a>Jie Wang, Jiu-Cheng Xie, Xianyan Li, Chi-Man Pun, Feng Xu, Hao Gao,  
  *[GaussianHead: High-fidelity Head Avatars with Learnable Gaussian Derivation](https://arxiv.org/pdf/2312.01632.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.01632.pdf), [Project Page](https://chiehwangs.github.io/gaussian-head-page/), [Code](https://github.com/chiehwangs/gaussian-head)
- <a name="shenhan20230gaussianavatars"></a>Shenhan Qian, Tobias Kirschstein, Liam Schoneveld, Davide Davoli, Simon Giebenhain, Matthias Nießner,  
  *[GaussianAvatars: Photorealistic Head Avatars with Rigged 3D Gaussians](https://arxiv.org/pdf/2312.02069)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02069), [Project Page](https://shenhanqian.github.io/gaussian-avatars), [Code](https://github.com/ShenhanQian/GaussianAvatars), [Presentation](https://youtu.be/lVEY78RwU_I)
- <a name="shunyuan20230gpsgaussian"></a>Shunyuan Zheng, Boyao Zhou, Ruizhi Shao, Boning Liu, Shengping Zhang, Liqiang Nie, Yebin Liu,  
  *[GPS-Gaussian: Generalizable Pixel-wise 3D Gaussian Splatting for Real-time Human Novel View Synthesis](https://arxiv.org/pdf/2312.02155.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02155.pdf), [Project Page](https://github.com/ShunyuanZheng/GPS-Gaussian), [Code](https://github.com/ShunyuanZheng/GPS-Gaussian), [Presentation](https://youtu.be/TBIekcqt0j0)
- <a name="shoukang20230gauhuman"></a>Shoukang Hu Ziwei Liu,  
  *[GauHuman: Articulated Gaussian Splatting from Monocular Human Videos](https://arxiv.org/pdf/2312.02973.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02973.pdf), [Project Page](https://skhu101.github.io/GauHuman/), [Code](https://github.com/skhu101/GauHuman), [Presentation](https://www.youtube.com/embed/47772bgt5Xo)
- <a name="helisa20230headgas"></a>Helisa Dhamo, Yinyu Nie, Arthur Moreau, Jifei Song, Richard Shaw, Yiren Zhou, Eduardo Pérez-Pellitero,  
  *[HeadGaS: Real-Time Animatable Head Avatars via 3D Gaussian Splatting](https://arxiv.org/pdf/2312.02902.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02902.pdf)
- <a name="yuheng20230hifi4g"></a>Yuheng Jiang, Zhehao Shen, Penghao Wang, Zhuo Su, Yu Hong, Yingliang Zhang, Jingyi Yu, Lan Xu,  
  *[HiFi4G: High-Fidelity Human Performance Rendering via Compact Gaussian Splatting](https://arxiv.org/pdf/2312.03461.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.03461.pdf), [Project Page](https://nowheretrix.github.io/HiFi4G/), [Presentation](https://youtu.be/917WVr2EHh4)
- <a name="liangxiao20230gaussianavatar"></a>Liangxiao Hu, Hongwen Zhang, Yuxiang Zhang, Boyao Zhou, Boning Liu, Shengping Zhang, Liqiang Nie,  
  *[GaussianAvatar: Towards Realistic Human Avatar Modeling from a Single Video via Animatable 3D Gaussians](https://arxiv.org/pdf/2312.02134.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02134.pdf), [Project Page](https://huliangxiao.github.io/GaussianAvatar), [Code](https://github.com/huliangxiao/GaussianAvatar), [Presentation](https://www.youtube.com/watch?v=a4g8Z9nCF-k&t=1s)
- <a name="jun20230flashavatar"></a>Jun Xiang, Xuan Gao, Yudong Guo, Juyong Zhang,  
  *[FlashAvatar: High-Fidelity Digital Avatar Rendering at 300FPS](https://arxiv.org/pdf/2312.02134.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02134.pdf), [Project Page](https://ustc3dv.github.io/FlashAvatar/)
- <a name="shunsuke20230relightable"></a>Shunsuke Saito, Gabriel Schwartz, Tomas Simon, Junxuan Li, Giljoo Nam,  
  *[Relightable Gaussian Codec Avatars](https://arxiv.org/pdf/2312.03704.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.03704.pdf), [Project Page](https://shunsukesaito.github.io/rgca/)
- <a name="yufan20230monogaussianavatar"></a>Yufan Chen, Lizhen Wang, Qijing Li, Hongjiang Xiao, Shengping Zhang, Hongxun Yao, Yebin Liu,  
  *[MonoGaussianAvatar: Monocular Gaussian Point-based Head Avatar](https://arxiv.org/pdf/2312.04558.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.04558.pdf), [Project Page](https://yufan1012.github.io/MonoGaussianAvatar), [Code](https://github.com/yufan1012/MonoGaussianAvatar), [Presentation](https://youtu.be/3UvBkyPc-oc?si=SbveQKBLJh5GuhIY)
- <a name="haokai20230ash"></a>Haokai Pang, Heming Zhu, Adam Kortylewski, Christian Theobalt, Marc Habermann,  
  *[ASH: Animatable Gaussian Splats for Efficient and Photoreal Human Rendering](https://arxiv.org/pdf/2312.05941.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.05941.pdf), [Project Page](https://vcai.mpi-inf.mpg.de/projects/ash/), [Presentation](https://vcai.mpi-inf.mpg.de/projects/ash/videos/video_for_page.mp4)
- <a name="zhiyin202303dgsavatar"></a>Zhiyin Qian, Shaofei Wang, Marko Mihajlovic, Andreas Geiger, Siyu Tang,  
  *[3DGS-Avatar: Animatable Avatars via Deformable 3D Gaussian Splatting](https://arxiv.org/pdf/2312.09228.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.09228.pdf), [Project Page](https://neuralbodies.github.io/3DGS-Avatar/index.html), [Code](https://github.com/mikeqzy/3dgs-avatar-release), [Presentation](https://youtu.be/FJ29U9OkmmU?si=5ua2mtpv5ei2n28Z)
- <a name="ye20230gavatar"></a>Ye Yuan, Xueting Li, Yangyi Huang, Shalini De Mello, Koki Nagano, Jan Kautz, Umar Iqbal,  
  *[GAvatar: Animatable 3D Gaussian Avatars with Implicit Mesh Learning](https://arxiv.org/pdf/2312.11461.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.11461.pdf), [Project Page](https://nvlabs.github.io/GAvatar/), [Presentation](https://www.youtube.com/watch?v=PbCF1HzrKrs)
- <a name="hyunjun20230deformable"></a>HyunJun Jung, Nikolas Brasch, Jifei Song, Eduardo Perez-Pellitero, Yiren Zhou, Zhihao Li, Nassir Navab, Benjamin Busam,  
  *[Deformable 3D Gaussian Splatting for Animatable Human Avatars](https://arxiv.org/pdf/2312.15059.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.15059.pdf)
- <a name="mingwei20230human101"></a>Mingwei Li, Jiachen Tao, Zongxin Yang, Yi Yang,  
  *[Human101: Training 100+FPS Human Gaussians in 100s from 1 View](https://arxiv.org/pdf/2312.15258.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.15258.pdf), [Project Page](https://longxiang-ai.github.io/Human101/), [Code](https://github.com/longxiang-ai/Human101)
- <a name="yuelang20230gaussian"></a>Yuelang Xu, Benwang Chen, Zhe Li, Hongwen Zhang, Lizhen Wang, Zerong Zheng, Yebin Liu,  
  *[Gaussian Head Avatar: Ultra High-fidelity Head Avatar via Dynamic Gaussians](https://arxiv.org/pdf/2312.03029.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.03029.pdf), [Project Page](https://yuelangx.github.io/gaussianheadavatar/), [Code](https://github.com/YuelangX/Gaussian-Head-Avatar), [Presentation](https://www.youtube.com/watch?v=kvrrI3EoM5g)

<a name="classic-work"></a>
# Classic work
- <a name="james20230a"></a>James F. Blinn,  
  *[A Generalization of Algebraic Surface Drawing](https://dl.acm.org/doi/pdf/10.1145/357306.357310)*,  
  2023, [PDF](https://dl.acm.org/doi/pdf/10.1145/357306.357310)
- <a name="leonid20230approximate"></a>Leonid Keselman and Martial Hebert,  
  *[Approximate Differentiable Rendering with Algebraic Surfaces](https://arxiv.org/pdf/2207.10606.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2207.10606.pdf), [Project Page](https://leonidk.com/fuzzy-metaballs/), [Code](https://github.com/leonidk/fuzzy-metaballs), [Presentation](https://www.youtube.com/watch?v=Ec7cxEc9eOU)
- <a name="jan20230unbiased"></a>Jan U. Müller, Michael Weinmann, Reinhard Klein,  
  *[Unbiased Gradient Estimation for Differentiable Surface Splatting via Poisson Sampling](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136930276.pdf)*,  
  2023, [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136930276.pdf), [Code](https://github.com/muellerju/unbiased-differentiable-splatting)
- <a name="petr20230generating"></a>Petr Man,  
  *[Generating and Real-Time Rendering of Clouds](https://old.cescg.org/CESCG-2006/papers/Prague-Man-Petr.pdf)*,  
  2023, [PDF](https://old.cescg.org/CESCG-2006/papers/Prague-Man-Petr.pdf)

<a name="compression"></a>
# Compression
- <a name="simon20240compressed"></a>Simon Niedermayr, Josef Stumpfegger, Rüdiger Westermann,  
  *[Compressed 3D Gaussian Splatting for Accelerated Novel View Synthesis](https://arxiv.org/pdf/2401.02436.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.02436.pdf), [Project Page](https://keksboter.github.io/c3dgs/), [Code](https://github.com/KeKsBoTer/c3dgs)
- <a name="yihang20240hac"></a>Yihang Chen, Qianyi Wu, Jianfei Cai, Mehrtash Harandi, Weiyao Lin,  
  *[HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression](https://arxiv.org/pdf/2401.02436.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.02436.pdf), [Project Page](https://yihangchen-ee.github.io/project_hac/), [Code](https://github.com/YihangChen-ee/HAC)
- <a name="zhiwen20230lightgaussian"></a>Zhiwen Fan, Kevin Wang, Kairun Wen, Zehao Zhu, Dejia Xu, Zhangyang Wang,  
  *[LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS](https://arxiv.org/pdf/2311.17245.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17245.pdf), [Project Page](https://lightgaussian.github.io/), [Code](https://github.com/VITA-Group/LightGaussian), [Presentation](https://youtu.be/470hul75bSM?si=EKm-UaBaTs9qJH6K)
- <a name="kl20230compact3d"></a>KL Navaneet, Kossar Pourahmadi Meibodi, Soroush Abbasi Koohpayegani, Hamed Pirsiavash,  
  *[Compact3D: Compressing Gaussian Splat Radiance Field Models with Vector Quantization](https://arxiv.org/pdf/2311.18159.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.18159.pdf), [Code](https://github.com/UCDvision/compact3d)
- <a name="joo20230compact"></a>Joo Chan Lee, Daniel Rho, Xiangyu Sun, Jong Hwan Ko, Eunbyung Park,  
  *[Compact 3D Gaussian Representation for Radiance Field](https://arxiv.org/pdf/2311.13681.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.13681.pdf), [Project Page](https://maincold2.github.io/c3dgs/), [Code](https://github.com/maincold2/Compact-3DGS)
- <a name="wieland20230compact"></a>Wieland Morgenstern, Florian Barthel, Anna Hilsmann, Peter Eisert,  
  *[Compact 3D Scene Representation via Self-Organizing Gaussian Grids](https://arxiv.org/pdf/2312.13299.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.13299.pdf), [Project Page](https://fraunhoferhhi.github.io/Self-Organizing-Gaussians/), [Code](https://github.com/fraunhoferhhi/Self-Organizing-Gaussians)

<a name="diffusion"></a>
# Diffusion
- <a name="dejia20240agg"></a>Dejia Xu, Ye Yuan, Morteza Mardani, Sifei Liu, Jiaming Song, Zhangyang Wang, Arash Vahdat,  
  *[AGG: Amortized Generative 3D Gaussians for Single Image to 3D](https://arxiv.org/pdf/2401.04099.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.04099.pdf), [Project Page](https://ir1d.github.io/AGG/), [Presentation](https://youtu.be/jkwmp2UH0Ug?si=lBXjme-d9bVrXTNf)
- <a name="zijie20240fast"></a>Zijie Pan, Zeyu Yang, Xiatian Zhu, Li Zhang,  
  *[Fast Dynamic 3D Object Generation from a Single-view Video](https://arxiv.org/pdf/2401.08742.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.08742.pdf), [Project Page](https://fudan-zvg.github.io/Efficient4D/), [Code](https://github.com/fudan-zvg/Efficient4D), [Presentation](https://fudan-zvg.github.io/Efficient4D/assets/video/demo.mp4)
- <a name="chen20240gaussianobject"></a>Chen Yang, Sikuang Li, Jiemin Fang, Ruofan Liang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian,  
  *[GaussianObject: Just Taking Four Images to Get A High-Quality 3D Object with Gaussian Splatting](https://arxiv.org/pdf/2402.10259.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.10259.pdf), [Project Page](https://gaussianobject.github.io/), [Code](https://github.com/GaussianObject/GaussianObject), [Presentation](https://youtu.be/ozoI0tmW3r0?si=KcaHtvVnrexqaf58)
- <a name="chen20240large"></a>Chen Yang, Sikuang Li, Jiemin Fang, Ruofan Liang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian,  
  *[Large Multi-View Gaussian Model for High-Resolution 3D Content Creation](https://arxiv.org/pdf/2402.05054.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.05054.pdf), [Project Page](https://me.kiui.moe/lgm/), [Code](https://github.com/3DTopia/LGM)
- <a name="xiaoyu20240gala3d"></a>Xiaoyu Zhou, Xingjian Ran, Yajiao Xiong, Jinlin He, Zhiwei Lin, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang,  
  *[GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting](https://arxiv.org/pdf/2402.07207.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.07207.pdf), [Project Page](https://gala3d.github.io/), [Code](https://github.com/VDIGPKU/GALA3D)
- <a name="luke20240im3d"></a>Luke Melas-Kyriazi, Iro Laina, Christian Rupprecht, Natalia Neverova, Andrea Vedaldi, Oran Gafni, Filippos Kokkinos,  
  *[IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation](https://arxiv.org/pdf/2402.08682.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.08682.pdf)
- <a name="zhiqi20240controllable"></a>Zhiqi Li, Yiming Chen, Lingzhe Zhao, Peidong Liu,  
  *[Controllable Text-to-3D Generation via Surface-Aligned Gaussian Splatting](https://lizhiqi49.github.io/MVControl/assets/paper.pdf)*,  
  2024, [PDF](https://lizhiqi49.github.io/MVControl/assets/paper.pdf), [Project Page](https://lizhiqi49.github.io/MVControl/), [Code](https://github.com/WU-CVGL/MVControl-threestudio)
- <a name="donglin20240hyper3dgtextto3d"></a>Donglin Di, Jiahui Yang, Chaofan Luo, Zhou Xue, Wei Chen, Xun Yang, Yue Gao,  
  *[Hyper-3DG:Text-to-3D Gaussian Generation via Hypergraph](https://arxiv.org/pdf/2403.09236.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.09236.pdf), [Code](https://github.com/yjhboy/Hyper3DG)
- <a name="haoran20240dreamscene"></a>Haoran Li, Haolin Shi, Wenli Zhang, Wenjun Wu, Yong Liao, Lin Wang, Lik Hang Lee, Pengyuan Zhou,  
  *[DreamScene: 3D Gaussian-based Text-to-3D Scene Generation via Formation Pattern Sampling](nan)*,  
  2024, [Project Page](https://dreamscene-project.github.io/)
- <a name="qijun20240fdgaussian"></a>Qijun Feng, Zhen Xing, Zuxuan Wu, Yu-Gang Jiang,  
  *[FDGaussian: Fast Gaussian Splatting from Single Image via Geometric-aware Diffusion Model](https://arxiv.org/pdf/2403.10242.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.10242.pdf), [Project Page](https://qjfeng.net/FDGaussian)
- <a name="tingyang20240bags"></a>Tingyang Zhang, Qingzhe Gao, Weiyu Li, Libin Liu, Baoquan Chen,  
  *[BAGS: Building Animatable Gaussian Splatting from a Monocular Video with Diffusion Priors](https://arxiv.org/pdf/2403.11427)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11427)
- <a name="lutao20240brightdreamer"></a>Lutao Jiang, Lin Wang,  
  *[BrightDreamer: Generic 3D Gaussian Generative Framework for Fast Text-to-3D Synthesis](https://arxiv.org/pdf/2403.11273)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11273), [Project Page](https://vlislab22.github.io/BrightDreamer/), [Code](https://github.com/lutao2021/BrightDreamer)
- <a name="xianglong20240gvgen"></a>Xianglong He, Junyi Chen, Sida Peng, Di Huang, Yangguang Li, Xiaoshui Huang, Chun Yuan, Wanli Ouyang, Tong He,  
  *[GVGEN: Text-to-3D Generation with Volumetric Representation](https://arxiv.org/pdf/2403.12957)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.12957), [Project Page](https://gvgen.github.io/), [Code](https://github.com/GVGEN/GVGEN)
- <a name="jaihoon20240synctweedies"></a>Jaihoon Kim, Juil Koo, Kyeongmin Yeo, Minhyuk Sung,  
  *[SyncTweedies: A General Generative Framework Based on Synchronized Diffusions](https://arxiv.org/pdf/2403.14370)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.14370), [Project Page](https://synctweedies.github.io/)
- <a name="dejia20240comp4d"></a>Dejia Xu, Hanwen Liang, Neel P. Bhatt, Hezhen Hu, Hanxue Liang, Konstantinos N. Plataniotis, Zhangyang Wang,  
  *[Comp4D: LLM-Guided Compositional 4D Scene Generation](https://arxiv.org/pdf/2403.16993.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.16993.pdf), [Project Page](https://vita-group.github.io/Comp4D/), [Code](https://github.com/VITA-Group/Comp4D), [Presentation](https://youtu.be/9q8SV1Xf_Xw)
- <a name="yuanze20240dreampolisher"></a>Yuanze Lin, Ronald Clark, Philip Torr,  
  *[DreamPolisher: Towards High-Quality Text-to-3D Generation via Geometric Diffusion](https://arxiv.org/pdf/2403.17237)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.17237), [Project Page](https://yuanze-lin.me/DreamPolisher_page/), [Code](https://github.com/yuanze-lin/DreamPolisher)
- <a name="zilong20230textto3d"></a>Zilong Chen, Feng Wang, Huaping Liu,  
  *[Text-to-3D using Gaussian Splatting](https://arxiv.org/pdf/2309.16585.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2309.16585.pdf), [Project Page](https://gsgen3d.github.io/), [Code](https://github.com/gsgen3d/gsgen), [Presentation](https://streamable.com/28snte)
- <a name="jiaxiang20230dreamgaussian"></a>Jiaxiang Tang, Jiawei Ren, Hang Zhou, Ziwei Liu, Gang Zeng,  
  *[DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://arxiv.org/pdf/2309.16653.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2309.16653.pdf), [Project Page](https://dreamgaussian.github.io/), [Code](https://github.com/dreamgaussian/dreamgaussian), [Presentation](https://www.youtube.com/live/l956ye13F8M?si=ZkvFL_lsY5OQUB7e)
- <a name="taoran20230gaussiandreamer"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[GaussianDreamer: Fast Generation from Text to 3D Gaussian Splatting with Point Cloud Priors](https://arxiv.org/pdf/2310.08529.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2310.08529.pdf), [Project Page](https://taoranyi.com/gaussiandreamer/), [Code](https://github.com/hustvl/GaussianDreamer)
- <a name="taoran20230gaussiandiffusion"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[GaussianDiffusion: 3D Gaussian Splatting for Denoising Diffusion Probabilistic Models with Structured Noise](https://arxiv.org/pdf/2311.11221.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.11221.pdf)
- <a name="taoran20230luciddreamer"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[LucidDreamer: Towards High-Fidelity Text-to-3D Generation via Interval Score Matching](https://arxiv.org/pdf/2311.11284.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.11284.pdf), [Code](https://github.com/EnVision-Research/LucidDreamer)
- <a name="taoran20230luciddreamer"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes](https://arxiv.org/pdf/2311.13384.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.13384.pdf), [Project Page](https://luciddreamer-cvlab.github.io/), [Code](https://github.com/anonymous-luciddreamer/LucidDreamer)
- <a name="taoran20230humangaussian"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting](https://arxiv.org/pdf/2311.17061.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17061.pdf), [Project Page](https://alvinliu0.github.io/projects/HumanGaussian), [Code](https://github.com/alvinliu0/HumanGaussian), [Presentation](https://www.youtube.com/watch?v=S3djzHoqPKY)
- <a name="taoran20230cg3d"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[CG3D: Compositional Generation for Text-to-3D](https://arxiv.org/pdf/2311.17907.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17907.pdf), [Project Page](https://asvilesov.github.io/CG3D/), [Presentation](https://www.youtube.com/watch?v=FMAVeolsE7s)
- <a name="taoran20230learn"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[Learn to Optimize Denoising Scores for 3D Generation - A Unified and Improved Diffusion Prior on NeRF and 3D Gaussian Splatting](https://arxiv.org/pdf/2312.04820.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.04820.pdf), [Project Page](https://yangxiaofeng.github.io/demo_diffusion_prior/), [Code](https://github.com/yangxiaofeng/LODS)
- <a name="taoran20230align"></a>Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,,  
  *[Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models](https://arxiv.org/pdf/2304.08818.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2304.08818.pdf), [Project Page](https://research.nvidia.com/labs/toronto-ai/AlignYourGaussians/)
- <a name="jiawei20230dreamgaussian4d"></a>Jiawei Ren, Liang Pan, Jiaxiang Tang, Chi Zhang, Ang Cao, Gang Zeng, Ziwei Liu,  
  *[DreamGaussian4D: Generative 4D Gaussian Splatting](https://arxiv.org/pdf/2312.17142.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.17142.pdf), [Project Page](https://jiawei-ren.github.io/projects/dreamgaussian4d/), [Code](https://github.com/jiawei-ren/dreamgaussian4d)
- <a name="yuyang202304dgen"></a>Yuyang Yin, Dejia Xu, Zhangyang Wang, Yao Zhao, Yunchao Wei,  
  *[4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency](https://arxiv.org/pdf/2312.17225.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.17225.pdf), [Project Page](https://vita-group.github.io/4DGen/), [Code](https://github.com/VITA-Group/4DGen), [Presentation](https://www.youtube.com/watch?v=-bXyBKdpQ1o)
- <a name="hao20230text2immersion"></a>Hao Ouyang, Kathryn Heal, Stephen Lombardi, Tiancheng Sun,  
  *[Text2Immersion: Generative Immersive Scene with 3D Gaussian](https://arxiv.org/pdf/2312.09242.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.09242.pdf), [Project Page](https://ken-ouyang.github.io/text2immersion/index.html)
- <a name="junwu20230repaint123"></a>Junwu Zhang, Zhenyu Tang, Yatian Pang, Xinhua Cheng, Peng Jin, Yida Wei, Munan Ning, Li Yuan,  
  *[Repaint123: Fast and High-quality One Image to 3D Generation with Progressive Controllable 2D Repainting](https://arxiv.org/pdf/2312.13271.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.13271.pdf), [Project Page](https://pku-yuangroup.github.io/repaint123/), [Code](https://github.com/PKU-YuanGroup/repaint123)

<a name="dynamics-and-deformation"></a>
# Dynamics and Deformation
- <a name="yuanxing202404d"></a>Yuanxing Duan, Fangyin Wei, Qiyu Dai, Yuhang He, Wenzheng Chen, Baoquan Chen,  
  *[4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes](https://arxiv.org/pdf/2402.03307.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.03307.pdf)
- <a name="quankai20240gaussianflow"></a>Quankai Gao, Qiangeng Xu, Zhe Cao, Ben Mildenhall, Wenchao Ma, Le Chen, Danhang Tang, Ulrich Neumann,  
  *[GaussianFlow: Splatting Gaussian Dynamics for 4D Content Creation](https://arxiv.org/pdf/2403.12365)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.12365), [Project Page](https://zerg-overmind.github.io/GaussianFlow.github.io/), [Code](https://github.com/Zerg-Overmind/GaussianFlow), [Presentation](https://www.youtube.com/watch?v=0qRcjTw7-YU)
- <a name="zhiyang20240motionaware"></a>Zhiyang Guo, Wengang Zhou, Li Li, Min Wang, Houqiang Li,  
  *[Motion-aware 3D Gaussian Splatting for Efficient Dynamic Scene Reconstruction](https://arxiv.org/pdf/2403.11447)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11447)
- <a name="yuting20240bridging"></a>Yuting Xiao, Xuan Wang, Jiafei Li, Hongrui Cai, Yanbo Fan, Nan Xue, Minghui Yang, Yujun Shen, Shenghua Gao,  
  *[Bridging 3D Gaussian and Mesh for Freeview Video Rendering](https://arxiv.org/pdf/2403.11453)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11453)
- <a name="jonathon20230dynamic"></a>Jonathon Luiten, Georgios Kopanas, Bastian Leibe, Deva Ramanan,  
  *[Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis](https://dynamic3dgaussians.github.io/paper.pdf)*,  
  2023, [PDF](https://dynamic3dgaussians.github.io/paper.pdf), [Project Page](https://dynamic3dgaussians.github.io/), [Code](https://github.com/JonathonLuiten/Dynamic3DGaussians), [Presentation](https://www.youtube.com/live/hDuy1TgD8I4?si=6oGN0IYnPRxOibpg)
- <a name="ziyi20230deformable"></a>Ziyi Yang, Xinyu Gao, Wen Zhou, Shaohui Jiao, Yuqing Zhang, Xiaogang Jin,  
  *[Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction](https://arxiv.org/pdf/2309.13101.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2309.13101.pdf), [Project Page](https://ingra14m.github.io/Deformable-Gaussians/), [Code](https://github.com/ingra14m/Deformable-3D-Gaussians)
- <a name="guanjun202304d"></a>Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Tian Qi, Xinggang Wang,  
  *[4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://arxiv.org/pdf/2310.08528.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2310.08528.pdf), [Project Page](https://guanjunwu.github.io/4dgs/), [Code](https://github.com/hustvl/4DGaussians)
- <a name="zeyu20230realtime"></a>Zeyu Yang, Hongye Yang, Zijie Pan, Xiatian Zhu, Li Zhang,  
  *[Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting](https://arxiv.org/pdf/2310.10642.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2310.10642.pdf), [Code](https://github.com/fudan-zvg/4d-gaussian-splatting)
- <a name="kai20230an"></a>Kai Katsumata, Duc Minh Vo, Hideki Nakayama,  
  *[An Efficient 3D Gaussian Representation for Monocular/Multi-view Dynamic Scenes](https://arxiv.org/pdf/2311.12897.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.12897.pdf), [Code](https://github.com/raven38/EfficientDynamic3DGaussian)
- <a name="agelos20230dynmf"></a>Agelos Kratimenos, Jiahui Lei, Kostas Daniilidis,  
  *[DynMF: Neural Motion Factorization for Real-time Dynamic View Synthesis with 3D Gaussian Splatting](https://arxiv.org/pdf/2312.00112.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.00112.pdf), [Project Page](https://agelosk.github.io/dynmf/), [Code](https://github.com/agelosk/dynmf)
- <a name="ruizhi20230control4d"></a>Ruizhi Shao, Jingxiang Sun, Cheng Peng, Zerong Zheng, Boyao Zhou, Hongwen Zhang, Yebin Liu,  
  *[Control4D: Efficient 4D Portrait Editing with Text](https://arxiv.org/pdf/2305.20082.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2305.20082.pdf), [Project Page](https://control4darxiv.github.io/)
- <a name="yihua20230scgs"></a>Yi-Hua Huang, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi,  
  *[SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://yihua7.github.io/SC-GS-web/materials/SC_GS_Arxiv.pdf)*,  
  2023, [PDF](https://yihua7.github.io/SC-GS-web/materials/SC_GS_Arxiv.pdf), [Project Page](https://yihua7.github.io/SC-GS-web/), [Code](https://github.com/yihua7/SC-GS)
- <a name="devikalyan20230neural"></a>Devikalyan Das, Christopher Wewer, Raza Yunus, Eddy Ilg, Jan Eric Lenssen,  
  *[Neural Parametric Gaussians for Monocular Non-Rigid Object Reconstruction](https://arxiv.org/pdf/2312.01196.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.01196.pdf)
- <a name="youtian20230gaussianflow"></a>Youtian Lin, Zuozhuo Dai, Siyu Zhu, Yao Yao,  
  *[Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle](https://arxiv.org/pdf/2310.08528.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2310.08528.pdf), [Project Page](https://nju-3dv.github.io/projects/Gaussian-Flow)
- <a name="heng20230cogs"></a>Heng Yu, Joel Julin, Zoltán Á. Milacski, Koichiro Niinuma, László A. Jeni,  
  *[CoGS: Controllable Gaussian Splatting](https://arxiv.org/pdf/2312.05664.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.05664.pdf), [Project Page](https://cogs2023.github.io/)
- <a name="yiqing20230gaufre"></a>Yiqing Liang, Numair Khan, Zhengqin Li, Thu Nguyen-Phuoc, Douglas Lanman, James Tompkin, Lei Xiao,  
  *[GauFRe: Gaussian Deformation Fields for Real-time Dynamic Novel View Synthesis](https://arxiv.org/pdf/2312.11458.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.11458.pdf), [Project Page](https://lynl7130.github.io/gaufre/index.html), [Presentation](https://youtu.be/YweWidWO8rI?si=jMssQdIXQV67kwzS)
- <a name="zhan20230spacetime"></a>Zhan Li, Zhang Chen, Zhong Li, Yi Xu,  
  *[Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis](https://arxiv.org/pdf/2312.16812.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.16812.pdf), [Project Page](https://oppo-us-research.github.io/SpacetimeGaussians-website/), [Code](https://github.com/oppo-us-research/SpacetimeGaussians), [Presentation](https://www.youtube.com/watch?v=YsPPmf-E6Lg)
- <a name="bardienus20230mdsplatting"></a>Bardienus P. Duisterhof, Zhao Mandi, Yunchao Yao, Jia-Wei Liu, Mike Zheng Shou, Shuran Song, Jeffrey Ichnowski,  
  *[MD-Splatting: Learning Metric Deformation from 4D Gaussians in Highly Deformable Scenes](https://arxiv.org/pdf/2312.00583)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.00583), [Project Page](https://md-splatting.github.io/), [Code](https://github.com/momentum-robotics-lab/md-splatting)
- <a name="richard20230swags"></a>Richard Shaw, Jifei Song, Arthur Moreau, Michal Nazarczuk, Sibi Catley-Chandar, Helisa Dhamo, Eduardo Perez-Pellitero,  
  *[SWAGS: Sampling Windows Adaptively for Dynamic 3D Gaussian Splatting](https://arxiv.org/pdf/2312.13308.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.13308.pdf)
- <a name="jiakai202303dgstream"></a>Jiakai Sun, Han Jiao, Guangyuan Li, Zhanjie Zhang, Lei Zhao, Wei Xing,  
  *[3DGStream: On-the-Fly Training of 3D Gaussians for Efficient Streaming of Photo-Realistic Free-Viewpoint Videos](https://arxiv.org/pdf/2403.01444.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2403.01444.pdf), [Project Page](https://sjojok.github.io/3dgstream/), [Code](https://github.com/SJoJoK/3DGStream)

<a name="editing"></a>
# Editing
- <a name="jingyu20240tipeditor"></a>Jingyu Zhuang, Di Kang, Yan-Pei Cao, Guanbin Li, Liang Lin, Ying Shan,  
  *[TIP-Editor: An Accurate 3D Editor Following Both Text-Prompts And Image-Prompts](https://arxiv.org/pdf/2401.14828.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.14828.pdf), [Project Page](https://zjy526223908.github.io/TIP-Editor/)
- <a name="xu20240segment"></a>Xu Hu, Yuxi Wang, Lue Fan, Junsong Fan, Junran Peng, Zhen Lei, Qing Li, Zhaoxiang Zhang,  
  *[Segment Anything in 3D Gaussians](https://browse.arxiv.org/pdf/2401.17857.pdf)*,  
  2024, [PDF](https://browse.arxiv.org/pdf/2401.17857.pdf)
- <a name="francesco20240gsedit"></a>Francesco Palandra, Andrea Sanchietti, Daniele Baieri, Emanuele Rodolà,  
  *[GSEdit: Efficient Text-Guided Editing of 3D Objects via Gaussian Splatting](https://arxiv.org/pdf/2403.05154.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.05154.pdf)
- <a name="jing20240gaussctrl"></a>Jing Wu, Jia-Wang Bian, Xinghui Li, Guangrun Wang, Ian Reid, Philip Torr, Victor Adrian Prisacariu,  
  *[GaussCtrl: Multi-View Consistent Text-Driven 3D Gaussian Splatting Editing](https://arxiv.org/pdf/2403.08733.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.08733.pdf)
- <a name="yuxuan20240viewconsistent"></a>Yuxuan Wang, Xuanyu Yi, Zike Wu, Na Zhao, Long Chen, Hanwang Zhang,  
  *[View-Consistent 3D Editing with Gaussian Splatting](https://arxiv.org/pdf/2403.11868.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11868.pdf)
- <a name="antoine20240gaussian"></a>Antoine Guédon, Vincent Lepetit,  
  *[Gaussian Frosting: Editable Complex Radiance Fields with Real-Time Rendering](https://arxiv.org/pdf/2403.14554)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.14554), [Project Page](https://anttwo.github.io/frosting/), [Code](https://github.com/Anttwo/Frosting), [Presentation](https://youtu.be/h7LeWq8sG78)
- <a name="jun20240semantic"></a>Jun Guo, Xiaojian Ma, Yue Fan, Huaping Liu, Qing Li,  
  *[Semantic Gaussians: Open-Vocabulary Scene Understanding with 3D Gaussian Splatting](https://arxiv.org/pdf/2403.15624)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.15624), [Project Page](https://semantic-gaussians.github.io/)
- <a name="yiwen20230gaussianeditor"></a>Yiwen Chen, Zilong Chen, Chi Zhang, Feng Wang, Xiaofeng Yang, Yikai Wang, Zhongang Cai, Lei Yang, Huaping Liu, Guosheng Lin,  
  *[GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting](https://arxiv.org/pdf/2311.14521.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.14521.pdf), [Project Page](https://buaacyw.github.io/gaussian-editor/), [Code](https://github.com/buaacyw/GaussianEditor), [Presentation](https://youtu.be/TdZIICSFqsU?si=-U4tyOvaAPqIROYn)
- <a name="jiemin20230gaussianeditor"></a>Jiemin Fang, Junjie Wang, Xiaopeng Zhang, Lingxi Xie, Qi Tian,  
  *[GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions](https://arxiv.org/pdf/2311.16037.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16037.pdf), [Project Page](https://gaussianeditor.github.io/), [Presentation](https://youtu.be/KWtALsigR3k?si=h6-A44brd5rm3_CM)
- <a name="jiajun20230pointn"></a>Jiajun Huang, Hongchuan Yu,  
  *[Point'n Move: Interactive Scene Object Manipulation on Gaussian Splatting Radiance Fields](https://arxiv.org/pdf/2311.16737.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16737.pdf)
- <a name="mingqiao20230gaussian"></a>Mingqiao Ye, Martin Danelljan, Fisher Yu, Lei Ke,  
  *[Gaussian Grouping: Segment and Edit Anything in 3D Scenes](https://arxiv.org/pdf/2312.00732.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.00732.pdf), [Code](https://github.com/lkeab/gaussian-grouping)
- <a name="jiazhong20230segment"></a>Jiazhong Cen, Jiemin Fang, Chen Yang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian,  
  *[Segment Any 3D Gaussians](https://jumpat.github.io/SAGA/SAGA_paper.pdf)*,  
  2023, [PDF](https://jumpat.github.io/SAGA/SAGA_paper.pdf), [Project Page](https://jumpat.github.io/SAGA/), [Code](https://github.com/Jumpat/SegAnyGAussians)
- <a name="shijie20230feature"></a>Shijie Zhou, Haoran Chang, Sicheng Jiang, Zhiwen Fan, Zehao Zhu, Dejia Xu, Pradyumna Chari, Suya You, Zhangyang Wang, Achuta Kadambi,  
  *[Feature 3DGS: Supercharging 3D Gaussian Splatting to Enable Distilled Feature Fields](https://arxiv.org/pdf/2312.03203.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.03203.pdf), [Project Page](https://feature-3dgs.github.io/), [Presentation](https://www.youtube.com/watch?v=YWZiF-WvMN4&t=4s)
- <a name="kun202302dguided"></a>Kun Lan, Haoran Li, Haolin Shi, Wenjun Wu, Yong Liao, Lin Wang, Pengyuan Zhou,  
  *[2D-Guided 3D Gaussian Segmentation](https://arxiv.org/pdf/2312.16047.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.16047.pdf)

<a name="language-embedding"></a>
# Language Embedding
- <a name="jinchuan20230language"></a>Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, Shao-Hua Guan,  
  *[Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding](https://arxiv.org/pdf/2311.18482.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.18482.pdf), [Project Page](https://buaavrcg.github.io/LEGaussians/)
- <a name="minghan20230langsplat"></a>Minghan Qin, Wanhua Li, Jiawei Zhou, Haoqian Wang, Hanspeter Pfister,  
  *[LangSplat: 3D Language Gaussian Splatting](https://arxiv.org/pdf/2312.16084.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.16084.pdf), [Project Page](https://langsplat.github.io/), [Code](https://github.com/minghanqin/LangSplat), [Presentation](https://www.youtube.com/watch?v=XMlyjsei-Es)
- <a name="xingxing20230fmgs"></a>Xingxing Zuo, Pouya Samangouei, Yunwen Zhou, Yan Di, Mingyang Li,  
  *[FMGS: Foundation Model Embedded 3D Gaussian Splatting for Holistic 3D Scene Understanding](https://arxiv.org/pdf/2401.01970.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2401.01970.pdf)

<a name="large-scale"></a>
# Large-Scale
- <a name="teppei20240fed3dgs"></a>Teppei Suzuki,  
  *[Fed3DGS: Scalable 3D Gaussian Splatting with Federated Learning](https://arxiv.org/pdf/2403.11460)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11460), [Code](https://github.com/dingdingcai/GS-pose)
- <a name="dingding20240gspose"></a>Dingding Cai, Janne Heikkilä, Esa Rahtu,  
  *[GS-Pose: Cascaded Framework for Generalizable Segmentation-based 6D Object Pose Estimation](https://arxiv.org/pdf/2403.10683)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.10683), [Project Page](https://dingdingcai.github.io/gs-pose/), [Code](https://github.com/dingdingcai/GS-pose), [Presentation](https://youtu.be/SnJazusDLM8)
- <a name="sai20240creating"></a>Sai Tarun Sathyan, Thomas B. Kinsman,  
  *[Creating Seamless 3D Maps Using Radiance Fields](https://arxiv.org/pdf/2403.11364.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11364.pdf)
- <a name="ke20240hgsmapping"></a>Ke Wu, Kaizhao Zhang, Zhiwei Zhang, Shanshuai Yuan, Muer Tie, Julong Wei, Zijun Xu, Jieru Zhao, Zhongxue Gan, Wenchao Ding,  
  *[HGS-Mapping: Online Dense Mapping Using Hybrid Gaussian Representation in Urban Scenes](https://arxiv.org/pdf/2403.20159.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.20159.pdf)
- <a name="yang20240citygaussian"></a>Yang Liu, He Guan, Chuanchen Luo, Lue Fan, Junran Peng, Zhaoxiang Zhang,  
  *[CityGaussian: Real-time High-quality Large-Scale Scene Rendering with Gaussians](https://arxiv.org/pdf/2403.20159.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.20159.pdf), [Project Page](https://dekuliutesla.github.io/citygs/)

<a name="mesh-extraction-and-physics"></a>
# Mesh Extraction and Physics
- <a name="yutao20240gaussian"></a>Yutao Feng, Xiang Feng, Yintong Shang, Ying Jiang, Chang Yu, Zeshun Zong, Tianjia Shao, Hongzhi Wu, Kun Zhou, Chenfanfu Jiang, Yin Yang,  
  *[Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting](https://browse.arxiv.org/pdf/2401.15318.pdf)*,  
  2024, [PDF](https://browse.arxiv.org/pdf/2401.15318.pdf), [Project Page](https://amysteriouscat.github.io/GaussianSplashing/), [Presentation](https://www.youtube.com/watch?v=KgaR1ni-Egg&t)
- <a name="joanna20240games"></a>Joanna Waczyńska, Piotr Borycki, Sławomir Tadeja, Jacek Tabor, Przemysław Spurek,  
  *[GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting](https://arxiv.org/pdf/2402.01459.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.01459.pdf), [Code](https://github.com/waczjoan/gaussian-mesh-splatting)
- <a name="lin20240meshbased"></a>Lin Gao, Jie Yang, Bo-Tao Zhang, Jia-Mu Sun, Yu-Jie Yuan, Hongbo Fu, Yu-Kun Lai,  
  *[Mesh-based Gaussian Splatting for Real-time Large-scale Deformation](https://arxiv.org/pdf/2402.04796.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.04796.pdf)
- <a name="licheng20240reconstruction"></a>Licheng Zhong, Hong-Xing Yu, Jiajun Wu, Yunzhu Li,  
  *[Reconstruction and Simulation of Elastic Objects with Spring-Mass 3D Gaussians](https://arxiv.org/pdf/2403.09434)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.09434), [Project Page](https://zlicheng.com/spring_gaus/), [Code](https://github.com/Colmar-zlicheng/Spring-Gaus)
- <a name="tianxing20240texturegs"></a>Tian-Xing Xu, Wenbo Hu, Yu-Kun Lai, Ying Shan, Song-Hai Zhang,  
  *[Texture-GS: Disentangling the Geometry and Texture for 3D Gaussian Splatting Editing](https://arxiv.org/pdf/2403.10050)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.10050), [Project Page](https://slothfulxtx.github.io/TexGS/), [Code](https://github.com/slothfulxtx/Texture-GS)
- <a name="matias20240dnsplatter"></a>Matias Turkulainen, Xuqian Ren, Iaroslav Melekhov, Otto Seiskari, Esa Rahtu, Juho Kannala,  
  *[DN-Splatter: Depth and Normal Priors for Gaussian Splatting and Meshing](https://arxiv.org/pdf/2403.17822)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.17822), [Code](https://github.com/maturk/dn-splatter)
- <a name="binbin202402d"></a>Binbin Huang, Zehao Yu, Anpei Chen, Andreas Geiger, Shenghua Gao,  
  *[2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://arxiv.org/pdf/2403.17888)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.17888), [Project Page](https://surfsplatting.github.io/), [Presentation](https://www.youtube.com/watch?v=oaHCtB6yiKU)
- <a name="rizhao20240feature"></a>Ri-Zhao Qiu, Ge Yang, Weijia Zeng, Xiaolong Wang,  
  *[Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing](https://arxiv.org/pdf/2404.01223)*,  
  2024, [PDF](https://arxiv.org/pdf/2404.01223), [Project Page](https://feature-splatting.github.io/), [Code](https://github.com/vuer-ai/feature_splatting)
- <a name="tianyi20230physgaussian"></a>Tianyi Xie, Zeshun Zong, Yuxin Qiu, Xuan Li, Yutao Feng, Yin Yang, Chenfanfu Jiang,  
  *[PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics](https://arxiv.org/pdf/2311.12198.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.12198.pdf), [Project Page](https://xpandora.github.io/PhysGaussian/), [Code](https://github.com/XPandora/PhysGaussian), [Presentation](https://drive.google.com/file/d/1eh7vxRxer7gfvPhs8jDE56oRjayBc9oe/view)
- <a name="antoine20230sugar"></a>Antoine Guédon, Vincent Lepetit,  
  *[SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering](https://arxiv.org/pdf/2311.12775.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.12775.pdf), [Project Page](https://imagine.enpc.fr/~guedona/sugar/), [Code](https://github.com/Anttwo/SuGaR), [Presentation](https://www.youtube.com/watch?v=MAkFyWfiBQo.&t)
- <a name="hanlin20230neusg"></a>Hanlin Chen, Chen Li, Gim Hee Lee,  
  *[NeuSG: Neural Implicit Surface Reconstruction with 3D Gaussian Splatting Guidance](https://arxiv.org/pdf/2312.00846.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.00846.pdf)

<a name="misc"></a>
# Misc
- <a name="van20240characterizing"></a>Van Minh Nguyen, Emma Sandidge, Trupti Mahendrakar, Ryan T. White,  
  *[Characterizing Satellite Geometry via Accelerated 3D Gaussian Splatting](https://arxiv.org/pdf/2401.02588.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.02588.pdf)
- <a name="linus20240trips"></a>Linus Franke, Darius Rückert, Laura Fink, Marc Stamminger,  
  *[TRIPS: Trilinear Point Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/pdf/2401.06003.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.06003.pdf), [Project Page](https://lfranke.github.io/trips/), [Code](https://github.com/lfranke/trips)
- <a name="lingting20240endogs"></a>Lingting Zhu, Zhao Wang, Jiahao Cui, Zhenchao Jin, Guying Lin, Lequan Yu,  
  *[EndoGS: Deformable Endoscopic Tissues Reconstruction with Gaussian Splatting](https://arxiv.org/pdf/2401.11535.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.11535.pdf), [Code](https://github.com/HKU-MedAI/EndoGS)
- <a name="yifan20240endogaussian"></a>Yifan Liu, Chenxin Li, Chen Yang, Yixuan Yuan,  
  *[EndoGaussian: Gaussian Splatting for Deformable Surgical Scene Reconstruction](https://arxiv.org/pdf/2401.12561.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.12561.pdf), [Project Page](https://yifliu3.github.io/EndoGaussian/), [Code](https://github.com/yifliu3/EndoGaussian)
- <a name="butian20240gauuscene"></a>Butian Xiong, Zhuo Li, Zhen Li,  
  *[GauU-Scene: A Scene Reconstruction Benchmark on Large Scale 3D Reconstruction Dataset Using Gaussian Splatting](https://arxiv.org/pdf/2401.14032.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.14032.pdf)
- <a name="sheng20240livgaussmap"></a>Sheng Hong, Junjie He, Xinhu Zheng, Hesheng Wang, Hao Fang, Kangcheng Liu, Chunran Zheng, Shaojie Shen,  
  *[LIV-GaussMap: LiDAR-Inertial-Visual Fusion for Real-time 3D Radiance Field Map Rendering](https://arxiv.org/pdf/2401.14857.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.14857.pdf), [Code](https://github.com/sheng00125/LIV-GaussMap)
- <a name="ying20240vrgs"></a>Ying Jiang, Chang Yu, Tianyi Xie, Xuan Li, Yutao Feng, Huamin Wang, Minchen Li, Henry Lau, Feng Gao, Yin Yang, Chenfanfu Jiang,  
  *[VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality](https://arxiv.org/pdf/2401.16663.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.16663.pdf), [Project Page](https://yingjiang96.github.io/VR-GS/)
- <a name="timothy20240splatnav"></a>Timothy Chen, Ola Shorinwa, Weijia Zeng, Joseph Bruno, Philip Dames, Mac Schwager,  
  *[Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](https://arxiv.org/pdf/2403.02751.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.02751.pdf)
- <a name="tyuanhao20240radiative"></a>TYuanhao Cai, Yixun Liang, Jiahao Wang, Angtian Wang, Yulun Zhang, Xiaokang Yang, Zongwei Zhou, Alan Yuille,  
  *[Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis](https://arxiv.org/pdf/2403.04116.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.04116.pdf)
- <a name="guanxing20240manigaussian"></a>Guanxing Lu, Shiyi Zhang, Ziwei Wang, Changliu Liu, Jiwen Lu, Yansong Tang,  
  *[ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](https://arxiv.org/pdf/2403.08321.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.08321.pdf), [Project Page](https://guanxinglu.github.io/ManiGaussian/), [Code](https://github.com/GuanxingLu/ManiGaussian)
- <a name="xinjie20240gaussianimage"></a>Xinjie Zhang, Xingtong Ge, Tongda Xu, Dailan He, Yan Wang, Hongwei Qin, Guo Lu, Jing Geng, Jun Zhang,  
  *[GaussianImage: 1000 FPS Image Representation and Compression by 2D Gaussian Splatting](https://arxiv.org/pdf/2403.08551)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.08551)
- <a name="yuhang20240gaussiangrasper"></a>Yuhang Zheng, Xiangyu Chen, Yupeng Zheng, Songen Gu, Runyi Yang, Bu Jin, Pengfei Li, Chengliang Zhong, Zengmao Wang, Lina Liu, Chao Yang, Dawei Wang, Zhen Chen, Xiaoxiao Long, Meiqing Wang,  
  *[GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping](https://arxiv.org/pdf/2403.09637)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.09637), [Code](https://github.com/MrSecant/GaussianGrasper)
- <a name="xiaohang20240densoft"></a>Xiaohang Yu, Zhengxian Yang, Shi Pan, Yuqi Han, Haoxiang Wang, Jun Zhang, Shi Yan, Borong Lin, Lei Yang, Tao Yu, Lu Fang,  
  *[Den-SOFT: Dense Space-Oriented Light Field DataseT for 6-DOF Immersive Experience](https://arxiv.org/pdf/2403.09973.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.09973.pdf)
- <a name="luca20240modeling"></a>Luca Savant, Diego Valsesia, Enrico Magli,  
  *[Modeling uncertainty for Gaussian Splatting](https://arxiv.org/pdf/2403.18476)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.18476)
- <a name="shuai20240togs"></a>Shuai Zhang, Huangxuan Zhao, Zhenghong Zhou, Guanjun Wu, Chuansheng Zheng, Xinggang Wang, Wenyu Liu,  
  *[TOGS: Gaussian Splatting with Temporal Opacity Offset for Real-Time 4D DSA Rendering](https://arxiv.org/pdf/2403.19586)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.19586)
- <a name="wen20230fisherrf"></a>Wen Jiang, Boshu Lei, Kostas Daniilidis,  
  *[FisherRF: Active View Selection and Uncertainty Quantification for Radiance Fields using Fisher Information](https://arxiv.org/pdf/2311.17874.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17874.pdf), [Project Page](https://jiangwenpl.github.io/FisherRF/), [Code](https://github.com/JiangWenPL/FisherRF)
- <a name="yurui20230periodic"></a>Yurui Chen, Chun Gu, Junzhe Jiang, Xiatian Zhu, Li Zhang,  
  *[Periodic Vibration Gaussian: Dynamic Urban Scene Reconstruction and Real-time Rendering](https://arxiv.org/pdf/2311.18561.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.18561.pdf), [Project Page](https://fudan-zvg.github.io/PVG/), [Code](https://github.com/fudan-zvg/PVG)
- <a name="chandradeep20230manus"></a>Chandradeep Pokhariya, Ishaan N Shah, Angela Xing, Zekun Li, Kefan Chen, Avinash Sharma, Srinath Sridhar,  
  *[MANUS: Markerless Hand-Object Grasp Capture using Articulated 3D Gaussians](https://arxiv.org/pdf/2312.02137.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02137.pdf)
- <a name="zixin20230triplane"></a>Zi-Xin Zou, Zhipeng Yu, Yuan-Chen Guo, Yangguang Li, Ding Liang, Yan-Pei Cao, Song-Hai Zhang,  
  *[Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers](https://arxiv.org/pdf/2312.09147.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.09147.pdf), [Project Page](https://zouzx.github.io/TriplaneGaussian/), [Code](https://github.com/VAST-AI-Research/TriplaneGaussian)
- <a name="vickie20230mathematical"></a>Vickie Ye, Angjoo Kanazawa,  
  *[Mathematical Supplement for the gsplat Library](https://arxiv.org/pdf/2312.02121.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02121.pdf)
- <a name="lukas20230pegasus"></a>Lukas Meyer, Floris Erich, Yusuke Yoshiyasu, Marc Stamminger, Noriaki Ando, Yukiyasu Domae,  
  *[PEGASUS: Physically Enhanced Gaussian Splatting Simulation System for 6DOF Object Pose Dataset Generation](https://arxiv.org/pdf/2401.02281.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2401.02281.pdf), [Project Page](https://meyerls.github.io/pegasus_web/), [Code](https://github.com/meyerls/PEGASUS)

<a name="navigation"></a>
# Navigation
- <a name="xiaohan20240gaussnav"></a>Xiaohan Lei, Min Wang, Wengang Zhou, Houqiang Li,  
  *[GaussNav: Gaussian Splatting for Visual Navigation](https://arxiv.org/pdf/2403.11625.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11625.pdf), [Project Page](https://xiaohanlei.github.io/projects/GaussNav/), [Code](https://xiaohanlei.github.io/projects/GaussNav/)
- <a name="peng202403dgsreloc"></a>Peng Jiang, Gaurav Pandey, Srikanth Saripalli,  
  *[3DGS-ReLoc: 3D Gaussian Splatting for Map Representation and Visual ReLocalization](https://arxiv.org/pdf/2403.11367)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11367)
- <a name="guangyi20240beyond"></a>Guangyi Liu, Wen Jiang, Boshu Lei, Vivek Pandey, Kostas Daniilidis, Nader Motee,  
  *[Beyond Uncertainty: Risk-Aware Active View Acquisition for Safe Robot Navigation and 3D Scene Understanding with FisherRF](https://arxiv.org/pdf/2403.11396)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11396)
- <a name="quentin202403dgscalib"></a>Quentin Herau, Moussab Bennehar, Arthur Moreau, Nathan Piasco, Luis Roldao, Dzmitry Tsishkou, Cyrille Migniot, Pascal Vasseur, Cédric Demonceaux,  
  *[3DGS-Calib: 3D Gaussian Splatting for Multimodal SpatioTemporal Calibration](https://arxiv.org/pdf/2403.11577)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11577)
- <a name="hongyu20240hugs"></a>Hongyu Zhou, Jiahao Shao, Lu Xu, Dongfeng Bai, Weichao Qiu, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao,  
  *[HUGS: Holistic Urban 3D Scene Understanding via Gaussian Splatting](https://arxiv.org/pdf/2403.12722.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.12722.pdf), [Project Page](https://xdimlab.github.io/hugs_website/)
- <a name="zhuopeng20240hogaussian"></a>Zhuopeng Li, Yilin Zhang, Chenming Wu, Jianke Zhu, Liangjun Zhang,  
  *[HO-Gaussian: Hybrid Optimization of 3D Gaussian Splatting for Urban Scenes](https://arxiv.org/pdf/2403.20032.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.20032.pdf)
- <a name="zhongrui20240sgd"></a>Zhongrui Yu, Haoran Wang, Jinze Yang, Hanzhang Wang, Zeke Xie, Yunfeng Cai, Jiale Cao, Zhong Ji, Mingming Sun,  
  *[SGD: Street View Synthesis with Gaussian Splatting and Diffusion Prior](https://arxiv.org/pdf/2403.20079.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.20079.pdf)

<a name="poses"></a>
# Poses
- <a name="hao20240ggrt"></a>Hao Li, Yuanyuan Gao, Dingwen Zhang, Chenming Wu, Yalun Dai, Chen Zhao, Haocheng Feng, Errui Ding, Jingdong Wang, Junwei Han,  
  *[GGRt: Towards Generalizable 3D Gaussians without Pose Priors in Real-Time](https://arxiv.org/pdf/2403.10147)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.10147), [Project Page](https://3d-aigc.github.io/GGRt/)
- <a name="dingding20240gspose"></a>Dingding Cai, Janne Heikkilä, Esa Rahtu,  
  *[GS-Pose: Cascaded Framework for Generalizable Segmentation-based 6D Object Pose Estimation](https://arxiv.org/pdf/2403.10683)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.10683), [Project Page](https://dingdingcai.github.io/gs-pose/), [Code](https://github.com/dingdingcai/GS-pose), [Presentation](https://youtu.be/SnJazusDLM8)

<a name="regularization-and-optimization"></a>
# Regularization and Optimization
- <a name="sankeerth20240distwar"></a>Sankeerth Durvasula, Adrian Zhao, Fan Chen, Ruofan Liang, Pawan Kumar Sanjaya, Nandita Vijaykumar,  
  *[DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines](https://arxiv.org/pdf/2401.05345.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.05345.pdf)
- <a name="jiahui20240fregs"></a>Jiahui Zhang, Fangneng Zhan, Muyu Xu, Shijian Lu, Eric Xing,  
  *[FreGS: 3D Gaussian Splatting with Progressive Frequency Regularization](https://arxiv.org/pdf/2403.06908.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.06908.pdf)
- <a name="jaewoo20240raings"></a>Jaewoo Jung, Jisang Han, Honggyu An, Jiwon Kang, Seonghoon Park, Seungryong Kim,  
  *[RAIN-GS: Relaxing Accurate Initialization Constraint for 3D Gaussian Splatting](https://arxiv.org/pdf/2403.09413)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.09413), [Project Page](https://ku-cvlab.github.io/RAIN-GS/), [Code](https://github.com/KU-CVLAB/RAIN-GS)
- <a name="qiyuan20240a"></a>Qiyuan Feng, Gengchen Cao, Haoxiang Chen, Tai-Jiang Mu, Ralph R. Martin, Shi-Min Hu,  
  *[A New Split Algorithm for 3D Gaussian Splatting](https://arxiv.org/pdf/2403.09143)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.09143)
- <a name="jaeyoung20230depthregularized"></a>Jaeyoung Chung, Jeongtaek Oh, Kyoung Mu Lee,  
  *[Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images](https://arxiv.org/pdf/2311.13398.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.13398.pdf), [Project Page](https://robot0321.github.io/DepthRegGS/index.html), [Code](https://github.com/robot0321/DepthRegularizedGS)
- <a name="sharath20230eagles"></a>Sharath Girish, Kamal Gupta, Abhinav Shrivastava,  
  *[EAGLES: Efficient Accelerated 3D Gaussians with Lightweight EncodingS](https://arxiv.org/pdf/2312.04564.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.04564.pdf), [Project Page](https://efficientgaussian.github.io/), [Code](https://github.com/Sharath-girish/efficientgaussian)
- <a name="yang20230colmapfree"></a>Yang Fu, Sifei Liu, Amey Kulkarni, Jan Kautz, Alexei A. Efros, Xiaolong Wang,  
  *[COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/pdf/2312.07504.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.07504.pdf), [Project Page](https://oasisyang.github.io/colmap-free-3dgs/), [Presentation](https://youtu.be/IJtnx4keJvg)
- <a name="yuan20230icomma"></a>Yuan Sun, Xuan Wang, Yunfan Zhang, Jie Zhang, Caigui Jiang, Yu Guo, Fei Wang,  
  *[iComMa: Inverting 3D Gaussians Splatting for Camera Pose Estimation via Comparing and Matching](https://arxiv.org/pdf/2312.09031.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.09031.pdf)

<a name="rendering"></a>
# Rendering
- <a name="luis20240gaussian"></a>Luis Bolanos, Shih-Yang Su, Helge Rhodin,  
  *[Gaussian Shadow Casting for Neural Characters](https://arxiv.org/pdf/2401.06116.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.06116.pdf)
- <a name="letian20240optimal"></a>Letian Huang, Jiayang Bai, Jie Guo, Yanwen Guo,  
  *[Optimal Projection for 3D Gaussian Splatting](https://browse.arxiv.org/pdf/2402.00752.pdf)*,  
  2024, [PDF](https://browse.arxiv.org/pdf/2402.00752.pdf)
- <a name="letian20240360gs"></a>Letian Huang, Jiayang Bai, Jie Guo, Yanwen Guo,  
  *[360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming](https://browse.arxiv.org/pdf/2402.00763.pdf)*,  
  2024, [PDF](https://browse.arxiv.org/pdf/2402.00763.pdf)
- <a name="lukas20240stopthepop"></a>Lukas Radl, Michael Steiner, Mathias Parger, Alexander Weinrauch, Bernhard Kerbl, Markus Steinberger,  
  *[StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering](arxiv.org/pdf/2402.00525.pdf)*,  
  2024, [PDF](arxiv.org/pdf/2402.00525.pdf), [Presentation](https://youtu.be/RJQlSORNkr0)
- <a name="abdullah20240ges"></a>Abdullah Hamdi, Luke Melas-Kyriazi, Guocheng Qian, Jinjie Mai, Ruoshi Liu, Carl Vondrick, Bernard Ghanem, Andrea Vedaldi,  
  *[GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering](https://arxiv.org/pdf/2402.10128.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.10128.pdf), [Project Page](https://abdullahamdi.com/ges/), [Code](https://github.com/ajhamdi/ges-splatting), [Presentation](https://youtu.be/edSvNy3roV8?si=VGncH7op1OfqkEtx)
- <a name="joongho20240identifying"></a>Joongho Jo, Hyeongwon Kim, Jongsun Park,  
  *[Identifying Unnecessary 3D Gaussians using Clustering for Fast Rendering of 3D Gaussian Splatting](https://arxiv.org/pdf/2402.13827.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.13827.pdf)
- <a name="kai20240gaussianpro"></a>Kai Cheng, Xiaoxiao Long, Kaizhi Yang, Yao Yao, Wei Yin, Yuexin Ma, Wenping Wang, Xuejin Chen,  
  *[GaussianPro: 3D Gaussian Splatting with Progressive Propagation](https://arxiv.org/pdf/2402.14650.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.14650.pdf), [Project Page](https://kcheng1021.github.io/gaussianpro.github.io/), [Code](https://github.com/kcheng1021/GaussianPro)
- <a name="ziyi20240specgaussian"></a>Ziyi Yang, Xinyu Gao, Yangtian Sun, Yihua Huang, Xiaoyang Lyu, Wen Zhou, Shaohui Jiao, Xiaojuan Qi, Xiaogang Jin,  
  *[Spec-Gaussian: Anisotropic View-Dependent Appearance for 3D Gaussian Splatting](https://arxiv.org/pdf/2402.15870.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.15870.pdf)
- <a name="jiaqi20240vastgaussian"></a>Jiaqi Lin, Zhihao Li, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Jiayue Liu, Yangdi Lu, Xiaofei Wu, Songcen Xu, Youliang Yan, Wenming Yang,  
  *[VastGaussian: Vast 3D Gaussians for Large Scene Reconstruction](https://arxiv.org/pdf/2402.17427.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.17427.pdf), [Project Page](https://vastgaussian.github.io/)
- <a name="xiangzhi202403d"></a>Xiangzhi Eric Wang, Zackary P. T. Sin,  
  *[3D Gaussian Model for Animation and Texturing](https://arxiv.org/pdf/2402.19441.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.19441.pdf)
- <a name="cheng20240bags"></a>Cheng Peng, Yutao Tang, Yifan Zhou, Nengyu Wang, Xijun Liu, Deming Li, Rama Chellappa,  
  *[BAGS: Blur Agnostic Gaussian Splatting through Multi-Scale Kernel Modeling](https://arxiv.org/pdf/2403.04926.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.04926.pdf)
- <a name="kunhao20240stylegaussian"></a>Kunhao Liu, Fangneng Zhan, Muyu Xu, Christian Theobalt, Ling Shao, Shijian Lu,  
  *[StyleGaussian: Instant 3D Style Transfer with Gaussian Splatting](https://arxiv.org/pdf/2403.04926.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.04926.pdf), [Project Page](https://kunhao-liu.github.io/StyleGaussian/), [Code](https://github.com/Kunhao-Liu/StyleGaussian)
- <a name="abhishek20240gaussian"></a>Abhishek Saroha, Mariia Gladkova, Cecilia Curreli, Tarun Yenamandra, Daniel Cremers,  
  *[Gaussian Splatting in Style](https://arxiv.org/pdf/2403.08498)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.08498)
- <a name="lingzhe20240badgaussians"></a>Lingzhe Zhao, Peng Wang, Peidong Liu,  
  *[BAD-Gaussians: Bundle Adjusted Deblur Gaussian Splatting](https://arxiv.org/pdf/2403.11831.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11831.pdf), [Project Page](https://lingzhezhao.github.io/BAD-Gaussians/), [Code](https://github.com/WU-CVGL/BAD-Gaussians/)
- <a name="hiba20240swag"></a>Hiba Dahmani, Moussab Bennehar, Nathan Piasco, Luis Roldao, Dzmitry Tsishkou,  
  *[SWAG: Splatting in the Wild images with Appearance-conditioned Gaussians](https://arxiv.org/pdf/2403.10427.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.10427.pdf)
- <a name="yanyan20240geogaussian"></a>Yanyan Li, Chenyu Lyu, Yan Di, Guangyao Zhai, Gim Hee Lee, Federico Tombari,  
  *[GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering](https://arxiv.org/pdf/2403.11324.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11324.pdf)
- <a name="zhihao20240analyticsplatting"></a>Zhihao Liang, Qi Zhang, Wenbo Hu, Ying Feng, Lei Zhu, Kui Jia,  
  *[Analytic-Splatting: Anti-Aliased 3D Gaussian Splatting via Analytic Integration](https://arxiv.org/pdf/2403.11056.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11056.pdf)
- <a name="otto20240gaussian"></a>Otto Seiskari, Jerry Ylilammi, Valtteri Kaatrasalo, Pekka Rantalankila, Matias Turkulainen, Juho Kannala, Esa Rahtu, Arno Solin,  
  *[Gaussian Splatting on the Move: Blur and Rolling Shutter Compensation for Natural Camera Motion](https://arxiv.org/pdf/2403.13327.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.13327.pdf), [Project Page](https://spectacularai.github.io/3dgs-deblur/), [Code](https://github.com/SpectacularAI/3dgs-deblur)
- <a name="michael20240radsplat"></a>Michael Niemeyer, Fabian Manhardt, Marie-Julie Rakotosaona, Michael Oechsle, Daniel Duckworth, Rama Gosula, Keisuke Tateno, John Bates, Dominik Kaeser, Federico Tombari,  
  *[RadSplat: Radiance Field-Informed Gaussian Splatting for Robust Real-Time Rendering with 900+ FPS](https://arxiv.org/pdf/2403.13806.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.13806.pdf), [Project Page](https://m-niemeyer.github.io/radsplat/)
- <a name="guangchi20240minisplatting"></a>Guangchi Fang, Bing Wang,  
  *[Mini-Splatting: Representing Scenes with a Constrained Number of Gaussians](https://arxiv.org/pdf/2403.14166.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.14166.pdf)
- <a name="zheng20240pixelgs"></a>Zheng Zhang, Wenbo Hu, Yixing Lao, Tong He, Hengshuang Zhao,  
  *[Pixel-GS: Density Control with Pixel-aware Gradient for 3D Gaussian Splatting](https://arxiv.org/pdf/2403.15530.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.15530.pdf)
- <a name="dongbin20240gaussian"></a>Dongbin Zhang, Chuming Wang, Weitao Wang, Peihao Li, Minghan Qin, Haoqian Wang,  
  *[Gaussian in the Wild: 3D Gaussian Splatting for Unconstrained Image Collections](https://arxiv.org/pdf/2403.15704)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.15704), [Project Page](https://eastbeanzhang.github.io/GS-W/), [Code](https://github.com/EastbeanZhang/Gaussian-Wild), [Presentation](https://www.youtube.com/watch?v=BNIX-OmIzgo)
- <a name="mulin20240gsdf"></a>Mulin Yu, Tao Lu, Linning Xu, Lihan Jiang, Yuanbo Xiangli, Bo Dai,  
  *[GSDF: 3DGS Meets SDF for Improved Rendering and Reconstruction](https://arxiv.org/pdf/2403.16964)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.16964), [Project Page](https://city-super.github.io/GSDF/), [Code](https://github.com/city-super/GSDF)
- <a name="kerui20240octreegs"></a>Kerui Ren, Lihan Jiang, Tao Lu, Mulin Yu, Linning Xu, Zhangkai Ni, Bo Dai,  
  *[Octree-GS: Towards Consistent Real-time Rendering with LOD-Structured 3D Gaussians](https://arxiv.org/pdf/2403.17898)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.17898), [Project Page](https://city-super.github.io/octree-gs/), [Code](https://github.com/city-super/Octree-GS)
- <a name="xiaowei20240sags"></a>Xiaowei Song, Jv Zheng, Shiran Yuan, Huan-ang Gao, Jingwei Zhao, Xiang He, Weihao Gu, Hao Zhao,  
  *[SA-GS: Scale-Adaptive Gaussian Splatting for Training-Free Anti-Aliasing](https://arxiv.org/pdf/2403.19615)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.19615), [Project Page](https://kevinsong729.github.io/project-pages/SA-GS/), [Code](https://github.com/zsy1987/SA-GS/)
- <a name="mauro20240snapit"></a>Mauro Comi, Alessio Tonioni, Max Yang, Jonathan Tremblay, Valts Blukis, Yijiong Lin, Nathan F. Lepora, Laurence Aitchison,  
  *[Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces](https://arxiv.org/pdf/2403.20275)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.20275)
- <a name="mauro20240snapit"></a>Mauro Comi, Alessio Tonioni, Max Yang, Jonathan Tremblay, Valts Blukis, Yijiong Lin, Nathan F. Lepora, Laurence Aitchison,  
  *[Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces](https://arxiv.org/pdf/2404.00409.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2404.00409.pdf), [Code](https://github.com/CVMI-Lab/3DGSR)
- <a name="jiarui20240mirror3dgs"></a>Jiarui Meng, Haijie Li, Yanmin Wu, Qiankun Gao, Shuzhou Yang, Jian Zhang, Siwei Ma,  
  *[Mirror-3DGS: Incorporating Mirror Reflections into 3D Gaussian Splatting](https://arxiv.org/pdf/2404.01168.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2404.01168.pdf)
- <a name="zehao20230mipsplatting"></a>Zehao Yu, Anpei Chen, Binbin Huang, Torsten Sattler, Andreas Geiger,  
  *[Mip-Splatting Alias-free 3D Gaussian Splatting](https://arxiv.org/pdf/2311.16493.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16493.pdf), [Project Page](https://niujinshuchong.github.io/mip-splatting/), [Code](https://github.com/autonomousvision/mip-splatting)
- <a name="jian20230relightable"></a>Jian Gao, Chun Gu, Youtian Lin, Hao Zhu, Xun Cao, Li Zhang, Yao Yao,  
  *[Relightable 3D Gaussian: Real-time Point Cloud Relighting with BRDF Decomposition and Ray Tracing](https://arxiv.org/pdf/2311.16043.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16043.pdf), [Project Page](https://nju-3dv.github.io/projects/Relightable3DGaussian/), [Code](https://github.com/NJU-3DV/Relightable3DGaussian)
- <a name="zhihao20230gsir"></a>Zhihao Liang, Qi Zhang, Ying Feng, Ying Shan, Kui Jia,  
  *[GS-IR: 3D Gaussian Splatting for Inverse Rendering](https://arxiv.org/pdf/2311.16473.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16473.pdf), [Project Page](https://github.com/lzhnb/GS-IR), [Code](https://github.com/lzhnb/GS-IR)
- <a name="zhiwen20230multiscale"></a>Zhiwen Yan, Weng Fei Low, Yu Chen, Gim Hee Lee,  
  *[Multi-Scale 3D Gaussian Splatting for Anti-Aliased Rendering](https://arxiv.org/pdf/2311.17089.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17089.pdf)
- <a name="yingwenqi20230gaussianshader"></a>Yingwenqi Jiang, Jiadong Tu, Yuan Liu, Xifeng Gao, Xiaoxiao Long, Wenping Wang, Yuexin Ma,  
  *[GaussianShader: 3D Gaussian Splatting with Shading Functions for Reflective Surfaces](https://arxiv.org/pdf/2311.17977.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.17977.pdf), [Project Page](https://asparagus15.github.io/GaussianShader.github.io/), [Code](https://github.com/Asparagus15/GaussianShader)
- <a name="tao20230scaffoldgs"></a>Tao Lu, Mulin Yu, Linning Xu, Yuanbo Xiangli, Limin Wang, Dahua Lin, Bo Dai,  
  *[Scaffold-GS: Structured 3D Gaussians for View-Adaptive Rendering](https://arxiv.org/pdf/2312.00109.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.00109.pdf), [Project Page](https://city-super.github.io/scaffold-gs/), [Code](https://github.com/city-super/Scaffold-GS)
- <a name="byeonghyeon20230deblurring"></a>Byeonghyeon Lee, Howoong Lee, Xiangyu Sun, Usman Ali, Eunbyung Park,  
  *[Deblurring 3D Gaussian Splatting](https://arxiv.org/pdf/2401.00834.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2401.00834.pdf), [Project Page](https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/), [Code](https://github.com/benhenryL/Deblurring-3D-Gaussian-Splatting)
- <a name="yahao20230gir"></a>Yahao Shi, Yanmin Wu, Chenming Wu, Xing Liu, Chen Zhao, Haocheng Feng, Jingtuo Liu, Liangjun Zhang, Jian Zhang, Bin Zhou, Errui Ding, Jingdong Wang,  
  *[GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization](https://arxiv.org/pdf/2312.05133)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.05133), [Project Page](https://3dgir.github.io/)
- <a name="dawid20230gaussian"></a>Dawid Malarz, Weronika Smolak, Jacek Tabor, Sławomir Tadeja, Przemysław Spurek,  
  *[Gaussian Splatting with NeRF-based Color and Opacity](https://arxiv.org/pdf/2312.13729.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.13729.pdf), [Code](https://github.com/gmum/ViewingDirectionGaussianSplatting)

<a name="reviews"></a>
# Reviews
- <a name="song20240progress"></a>Song Bai, Jie Li,  
  *[Progress and Prospects in 3D Generative AI: A Technical Overview including 3D human](https://arxiv.org/pdf/2401.02620.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.02620.pdf)
- <a name="guikun20240a"></a>Guikun Chen, Wenguan Wang,  
  *[A Survey on 3D Gaussian Splatting](https://arxiv.org/pdf/2401.03890.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2401.03890.pdf)
- <a name="ben202403d"></a>Ben Fei, Jingyi Xu, Rui Zhang, Qingyuan Zhou, Weidong Yang, Ying He,  
  *[3D Gaussian as a New Vision Era: A Survey](https://arxiv.org/pdf/2402.07181.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.07181.pdf)
- <a name="fabio20240how"></a>Fabio Tosi, Youmin Zhang, Ziren Gong, Erik Sandström, Stefano Mattoccia, Martin R. Oswald, Matteo Poggi,  
  *[How NeRFs and 3D Gaussian Splatting are Reshaping SLAM: a Survey](https://arxiv.org/pdf/2402.13255.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.13255.pdf)
- <a name="tong20240recent"></a>Tong Wu, Yu-Jie Yuan, Ling-Xiao Zhang, Jie Yang, Yan-Pei Cao, Ling-Qi Yan, Lin Gao,  
  *[Recent Advances in 3D Gaussian Splatting](https://arxiv.org/pdf/2403.11134.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11134.pdf)

<a name="slam"></a>
# SLAM
- <a name="mingrui20240sgsslam"></a>Mingrui Li, Shuhong Liu, Heng Zhou,  
  *[SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM](https://arxiv.org/pdf/2402.03246.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2402.03246.pdf)
- <a name="siting20240semgaussslam"></a>Siting Zhu, Renjie Qin, Guangming Wang, Jiuming Liu, Hesheng Wang,  
  *[SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM](https://arxiv.org/pdf/2403.07494.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.07494.pdf)
- <a name="tianchen20240compact"></a>Tianchen Deng, Yaohui Chen, Leyan Zhang, Jianfei Yang, Shenghai Yuan, Danwei Wang, Weidong Chen,  
  *[Compact 3D Gaussian Splatting For Dense Visual SLAM](https://arxiv.org/pdf/2403.11247.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11247.pdf)
- <a name="yiming20240nedsslam"></a>Yiming Ji, Yang Liu, Guanghu Xie, Boyu Ma, Zongwu Xie,  
  *[NEDS-SLAM: A Novel Neural Explicit Dense Semantic SLAM Framework using 3D Gaussian Splatting](https://arxiv.org/pdf/2403.11679.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.11679.pdf)
- <a name="shuo20240highfidelity"></a>Shuo Sun, Malcolm Mielle, Achim J. Lilienthal, Martin Magnusson,  
  *[High-Fidelity SLAM Using Gaussian Splatting with Rendering-Guided Densification and Regularized Optimization](https://arxiv.org/pdf/2403.12535.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.12535.pdf)
- <a name="seongbo20240rgbd"></a>Seongbo Ha, Jiung Yeon, Hyeonwoo Yu,  
  *[RGBD GS-ICP SLAM](https://arxiv.org/pdf/2403.12550.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.12550.pdf), [Code](https://github.com/Lab-of-AI-and-Robotics/GS_ICP_SLAM), [Presentation](https://youtu.be/e-bHh_uMMxE?si=bU4_Su4J91WQ2MEX)
- <a name="kailing20240endogslam"></a>Kailing Wang, Chen Yang, Yuehao Wang, Sikuang Li, Yan Wang, Qi Dou, Xiaokang Yang, Wei Shen,  
  *[EndoGSLAM: Real-Time Dense Reconstruction and Tracking in Endoscopic Surgeries using Gaussian Splatting](https://arxiv.org/pdf/2403.15124.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.15124.pdf), [Project Page](https://endogslam.loping151.com/), [Code](https://github.com/endogslam/EndoGSLAM)
- <a name="jiarui20240cgslam"></a>Jiarui Hu, Xianhao Chen, Boyin Feng, Guanglin Li, Liangjing Yang, Hujun Bao, Guofeng Zhang, Zhaopeng Cui,  
  *[CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field](https://arxiv.org/pdf/2403.16095)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.16095), [Project Page](https://zju3dv.github.io/cg-slam/), [Code](https://github.com/hjr37/CG-SLAM)
- <a name="lisong20240mm3dgs"></a>Lisong C. Sun, Neel P. Bhatt, Jonathan C. Liu, Zhiwen Fan, Zhangyang Wang, Todd E. Humphreys, Ufuk Topcu,  
  *[MM3DGS SLAM: Multi-modal 3D Gaussian Splatting for SLAM Using Vision, Depth, and Inertial Measurements](https://arxiv.org/pdf/2404.00923)*,  
  2024, [PDF](https://arxiv.org/pdf/2404.00923), [Project Page](https://vita-group.github.io/MM3DGS-SLAM/)
- <a name="chi20230gsslam"></a>Chi Yan, Delin Qu, Dong Wang, Dan Xu, Zhigang Wang, Bin Zhao, Xuelong Li,  
  *[GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting](https://arxiv.org/pdf/2311.11700.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.11700.pdf)
- <a name="nikhil20230splatam"></a>Nikhil Keetha, Jay Karhade, Krishna Murthy Jatavallabhula, Gengshan Yang,,  
  *[SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM](https://arxiv.org/pdf/2312.02126.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.02126.pdf), [Project Page](https://spla-tam.github.io/), [Code](https://github.com/spla-tam/SplaTAM), [Presentation](https://www.youtube.com/watch?v=35SX8DTdQLs)
- <a name="hidenobu20230gaussian"></a>Hidenobu Matsuki, Riku Murai, Paul H. J. Kelly, Andrew J. Davison,  
  *[Gaussian Splatting SLAM](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/dyson-robotics-lab/hide-et-al_GaussianSplattingSLAM_Dec2023.pdf)*,  
  2023, [PDF](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/dyson-robotics-lab/hide-et-al_GaussianSplattingSLAM_Dec2023.pdf), [Project Page](https://rmurai.co.uk/projects/GaussianSplattingSLAM/), [Code](https://github.com/muskie82/MonoGS), [Presentation](https://youtu.be/x604ghp9R_Q?si=fPtz4kgBKFfcnQf3)
- <a name="vladimir20230gaussianslam"></a>Vladimir Yugay, Yue Li, Theo Gevers, Martin R. Oswald,  
  *[Gaussian-SLAM: Photo-realistic Dense SLAM with Gaussian Splatting](https://ivi.fnwi.uva.nl/cv/paper/GaussianSLAM.pdf)*,  
  2023, [PDF](https://ivi.fnwi.uva.nl/cv/paper/GaussianSLAM.pdf), [Project Page](https://vladimiryugay.github.io/gaussian_slam/), [Code](https://github.com/VladimirYugay/Gaussian-SLAM), [Presentation](https://www.youtube.com/watch?v=RZK1o_ija7M)
- <a name="huajian20230photoslam"></a>Huajian Huang, Longwei Li, Hui Cheng, Sai-Kit Yeung,  
  *[Photo-SLAM: Real-time Simultaneous Localization and Photorealistic Mapping for Monocular, Stereo, and RGB-D Cameras](https://arxiv.org/pdf/2311.16728.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2311.16728.pdf)

<a name="seminal-paper-introducing-3d-gaussian-splatting"></a>
# Seminal Paper introducing 3D Gaussian Splatting
- <a name="bernhardnangaussian"></a>Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis,  
  *[Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf)*,  
  , [PDF](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf), [Project Page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/), [Code](https://github.com/graphdeco-inria/gaussian-splatting), [Presentation](https://youtu.be/T_kXY43VZnk?si=DrkbDFxQAv5scQNT)

<a name="sparse"></a>
# Sparse
- <a name="jiahe20240dngaussian"></a>Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Xin Ning, Jun Zhou, Lin Gu,  
  *[DNGaussian: Optimizing Sparse-View 3D Gaussian Radiance Fields with Global-Local Depth Normalization](https://arxiv.org/pdf/2403.06912.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.06912.pdf), [Project Page](https://fictionarry.github.io/DNGaussian/), [Code](https://github.com/Fictionarry/DNGaussian), [Presentation](https://www.youtube.com/watch?v=WKXCFNJHZ4o)
- <a name="aiden20240touchgs"></a>Aiden Swann, Matthew Strong, Won Kyung Do, Gadiel Sznaier Camps, Mac Schwager, Monroe Kennedy III,  
  *[Touch-GS: Visual-Tactile Supervised 3D Gaussian Splatting](https://arxiv.org/pdf/2403.09875.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.09875.pdf), [Project Page](https://armlabstanford.github.io/touch-gs)
- <a name="yuedong20240mvsplat"></a>Yuedong Chen, Haofei Xu, Chuanxia Zheng, Bohan Zhuang, Marc Pollefeys, Andreas Geiger, Tat-Jen Cham, Jianfei Cai,  
  *[MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/pdf/2403.14627)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.14627), [Project Page](https://donydchen.github.io/mvsplat/), [Code](https://github.com/donydchen/mvsplat)
- <a name="christopher20240latentsplat"></a>Christopher Wewer, Kevin Raj, Eddy Ilg, Bernt Schiele, Jan Eric Lenssen,  
  *[latentSplat: Autoencoding Variational Gaussians for Fast Generalizable 3D Reconstruction](https://arxiv.org/pdf/2403.16292.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.16292.pdf), [Project Page](https://geometric-rl.mpi-inf.mpg.de/latentsplat/)
- <a name="yinghao20240grm"></a>Yinghao Xu, Zifan Shi, Wang Yifan, Hansheng Chen, Ceyuan Yang, Sida Peng, Yujun Shen, Gordon Wetzstein,  
  *[GRM: Large Gaussian Reconstruction Model for Efficient 3D Reconstruction and Generation](https://arxiv.org/pdf/2403.14621.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.14621.pdf), [Project Page](https://justimyhxu.github.io/projects/grm/), [Code](https://github.com/justimyhxu/grm)
- <a name="qiuhong20240gamba"></a>Qiuhong Shen, Xuanyu Yi, Zike Wu, Pan Zhou, Hanwang Zhang, Shuicheng Yan, Xinchao Wang,  
  *[Gamba: Marry Gaussian Splatting with Mamba for single view 3D reconstruction](https://arxiv.org/pdf/2403.18795)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.18795)
- <a name="avinash20240coherentgs"></a>Avinash Paliwal, Wei Ye, Jinhui Xiong, Dmytro Kotovenko, Rakesh Ranjan, Vikas Chandra, Nima Khademi Kalantari,  
  *[CoherentGS: Sparse Novel View Synthesis with Coherent 3D Gaussians](https://arxiv.org/pdf/2403.19495)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.19495), [Project Page](https://people.engr.tamu.edu/nimak/Papers/CoherentGS/index.html)
- <a name="bowen20240gaussiancube"></a>Bowen Zhang, Yiji Cheng, Jiaolong Yang, Chunyu Wang, Feng Zhao, Yansong Tang, Dong Chen, Baining Guo,  
  *[GaussianCube: Structuring Gaussian Splatting using Optimal Transport for 3D Generative Modeling](https://arxiv.org/pdf/2403.19655.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.19655.pdf), [Project Page](https://gaussiancube.github.io/), [Code](https://github.com/GaussianCube/GaussianCube)
- <a name="zhiwen20240instantsplat"></a>Zhiwen Fan, Wenyan Cong, Kairun Wen, Kevin Wang, Jian Zhang, Xinghao Ding, Danfei Xu, Boris Ivanovic, Marco Pavone, Georgios Pavlakos, Zhangyang Wang, Yue Wang,  
  *[InstantSplat: Unbounded Sparse-view Pose-free Gaussian Splatting in 40 Seconds](https://arxiv.org/pdf/2403.20309.pdf)*,  
  2024, [PDF](https://arxiv.org/pdf/2403.20309.pdf), [Project Page](https://instantsplat.github.io/)
- <a name="haolin20230sparsegs"></a>Haolin Xiong, Sairisheek Muttukuru, Rishi Upadhyay, Pradyumna Chari, Achuta Kadambi,  
  *[SparseGS: Real-Time 360° Sparse View Synthesis using Gaussian Splatting](https://arxiv.org/pdf/2312.00206.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.00206.pdf), [Project Page](https://formycat.github.io/SparseGS-Real-Time-360-Sparse-View-Synthesis-using-Gaussian-Splatting/)
- <a name="zehao20230fsgs"></a>Zehao Zhu, Zhiwen Fan, Yifan Jiang, Zhangyang Wang,  
  *[FSGS: Real-Time Few-shot View Synthesis using Gaussian Splatting](https://arxiv.org/pdf/2312.00451.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.00451.pdf), [Project Page](https://zehaozhu.github.io/FSGS/), [Code](https://github.com/VITA-Group/FSGS)
- <a name="david20230pixelsplat"></a>David Charatan, Sizhe Li, Andrea Tagliasacchi, Vincent Sitzmann,  
  *[pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction](https://arxiv.org/pdf/2312.12337.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.12337.pdf), [Project Page](https://davidcharatan.com/pixelsplat/), [Code](https://github.com/dcharatan/pixelsplat)
- <a name="stanislaw20230splatter"></a>Stanislaw Szymanowicz, Christian Rupprecht, Andrea Vedaldi,  
  *[Splatter Image: Ultra-Fast Single-View 3D Reconstruction](https://arxiv.org/pdf/2312.13150.pdf)*,  
  2023, [PDF](https://arxiv.org/pdf/2312.13150.pdf), [Project Page](https://szymanowiczs.github.io/splatter-image.html), [Code](https://github.com/szymanowiczs/splatter-image), [Presentation](https://www.youtube.com/watch?v=pcKTf9SVh4g)