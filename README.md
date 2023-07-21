# SoftWareCopyRightDemo
## 运行方式
```shell
git clone https://github.com/MosRat/SoftWareCopyRightDemo

conda create -n qtfluentui python=3.8.10

pip install -r requirements.txt

python main.py
```
## UI设计器
仓库主目录打开终端：

```shell
python ./PyQt-Fluent-Widgets/tools/designer.py
```

在出现的QtDesigner中选择打开`demo1.ui`

注意使用fluentUI控件（下面的那些）

使用`pyuic`转换ui文件为py文件（使用方式取决于你的IDE或者终端，自行百度）

参考`FocusInterFace.py`中多重继承和初始化的写法，定义一个页面类

参考`main.py`中的写法，将页面添加到窗口

## 参考资料

fluentUI设计包  https://pyqt-fluent-widgets.readthedocs.io/zh_CN/latest/

PyQt5教程 https://maicss.gitbook.io/pyqt-chinese-tutoral/pyqt5/

PyQt+Designer配置 https://zhuanlan.zhihu.com/p/269273821

QtDesigner教程 https://zhuanlan.zhihu.com/p/348032800
