# HBM Predictor

## 简介

本项目为厦门大学与华为2012庞加莱实验室的合作项目产出成果。成果已发表于USENIX ATC'24上的论文"Removing Obstacles before Breaking Through the Memory Wall: A Close Look at HBM Errors in the Field"。该项目实现了多层次的HBM预测器、分析框架以及相关数据集，所实现的预测器是一个分层级的、全方位的、非侵入式的针对HBM故障设计的故障预测框架。

## 数据集描述
为了鼓励更多的研究人员探索HBM故障的相关特征，我们公开了从19个数据中心收集到的数据集。数据集包含在`Data`文件夹中，并分为两部分：

&nbsp;&nbsp;&nbsp;&nbsp;● **processed_data**  包含四个 CSV 文件，其中包含从不同层级生成的特征和标签： `data_for_bank-level_prediction.csv`, `data_for_col-level_prediction.csv`，`data_for_row-level_prediction.csv`，和`data_for_server-level_prediction.csv`. 例如，`data_for_bank-level_prediction` 是用于从bank层面进行预测的数据，如下方表格所示：

| Peak Power  | Aver Power  | Temp        | CE_Row | CE_Col | CE_Cell | UER_Row | UER_Col | UER_Cell | UEO_Row | UEO_Col | UEO_Cell | All_Row | All_Col | All_Cell | SID_0 | SID_1 | label |
| ----------- | ----------- | ----------- | ------ | ------ | ------- | ------- | ------- | -------- | ------- | ------- | -------- | ------- | ------- | -------- | ----- | ----- | ----- |
| 1           | 1           | 1           | 1      | 1      | 1       | 0       | 0       | 0        | 0       | 0       | 0        | 1       | 1       | 1        | 1     | 0     | 0     |
| 1.036677418 | 1.035688311 | 0.992300485 | 1      | 1      | 1       | 0       | 0       | 0        | 0       | 0       | 0        | 1       | 1       | 1        | 1     | 0     | 0     |

&nbsp;&nbsp;&nbsp;&nbsp;● **raw_data**  仅包含一个 CSV 文件，其中包含有关错误发生的位置、时间和类型的具体信息。数据格式示例如下所示：

| Datacenter  | Server      | Name | Stack | SID  | PcId | BankGroup | BankArray | Col  | Row    | Time       | EccType |
| ----------- | ----------- | ---- | ----- | ---- | ---- | --------- | --------- | ---- | ------ | ---------- | ------- |
| Datacenter8 | 0.108.38.22 | DSA3 | 0x3   | 0x0  | 0x1  | 0x2       | 0x1       | 0x54 | 0x3e2b | 1650690000 | UER     |
| Datacenter8 | 0.108.38.22 | DSA3 | 0x3   | 0x0  | 0x1  | 0x2       | 0x1       | 0x5c | 0x3fbb | 1650690000 | UER     |
| Datacenter0 | 0.0.0.16    | DSA8 | 0x0   | 0x0  | 0x4  | 0x2       | 0x3       | 0x58 | 0x2a57 | 1652709600 | CE      |

__请注意，__ 我们对数据集中的一些信息进行了脱敏处理，以避免敏感信息遭到泄露。

## 分析和预测

以下部分将指导您如何在本地设备上运行预测代码：

### 相关依赖安装

要运行此项目，请确保您的系统安装了 Python 3.6 或更高版本。然后在项目路径下执行以下命令以安装所需的库：

```
pip3 install -r requirements.txt
```



## 源代码结构

本项目的代码被分为两部分：

- **analyses**:  包含九个分析不同错误特征的代码文件。
  - `avg_temp_distribution.py` 
  - `ce_storm_machine.py` 
  - `dataset_analyze.py` 
  - `error_mode.py` 
  - `max_temp_distribution.py` 
  - `power_impact.py` 
  - `spatial_locality.py` 
  - `structure_impact.py` 
  - `time_between_error.py`
- **prediction**: 包含四个对不同参数设置下__HBM预测器__的性能进行实验测试的代码文件。
  - `prediction_performance.py`

  - `diff_model.py` 

  - `diff_observation_window.py` 

  - `diff_prediction_window.py` 

**请注意，**文件名代表分析或预测的类型。 例如，`prediction_performance.py`代表测试__HBM预测器__的预测性能。

## 运行

如果您想运行相关代码，请执行以下命令：

```
cd <folder>
python3 <filename>.py
```

例如，如果需要测试 __Calchas__ 的预测性能，可以执行以下命令：

```
cd prediction
python3 prediction_performance.py
```

随后可以在控制台得到如下输出：

```
=======Test1 for each predictor=======

Results of row-level predictor (Precision, Recall, F1_score)
RF with threshold=0.55: 0.6979166666666666, 0.881578947368421, 0.7790697674418604
Default RF: 0.53125, 0.8947368421052632, 0.6666666666666666

Results of col-level predictor (Precision, Recall, F1_score)
RF with threshold=0.6: 0.7267080745341615, 0.8666666666666667, 0.7905405405405406
Default RF: 0.7166666666666667, 0.9555555555555556, 0.8190476190476191

Results of bank-level predictor (Precision, Recall, F1_score)
RF with threshold=0.55: 0.6681034482758621, 0.7380952380952381, 0.7013574660633485
Default RF: 0.6681034482758621, 0.7380952380952381, 0.7013574660633485

Results of server-level predictor (Precision, Recall, F1_score)
RF with threshold=0.6: 0.3325581395348837, 0.5674603174603174, 0.4193548387096774
Default RF: 0.2826510721247563, 0.5753968253968254, 0.3790849673202614
```

由于预测模型使用的是机器学习模型，因此每次运行得到的预测结果可能会有所不同。

## 引用
如果您使用了我们论文中公开的数据集，请您引用我们的论文，谢谢。

```
@inproceedings {298591,
author = {Ronglong Wu and Shuyue Zhou and Jiahao Lu and Zhirong Shen and Zikang Xu and Jiwu Shu and Kunlin Yang and Feilong Lin and Yiming Zhang},
title = {Removing Obstacles before Breaking Through the Memory Wall: A Close Look at {HBM} Errors in the Field},
booktitle = {2024 USENIX Annual Technical Conference (USENIX ATC 24)},
year = {2024},
isbn = {978-1-939133-41-0},
address = {Santa Clara, CA},
pages = {851--867},
url = {https://www.usenix.org/conference/atc24/presentation/wu-ronglong},
publisher = {USENIX Association},
month = jul
}
```

