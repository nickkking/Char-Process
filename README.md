# char-process
拿到一堆线粒体rna的coI序列，由于全部序列都放在一个txt文件里面，因为后期需要把每一个序列单独拿出来fas文件，然后根据一个表格分类到种。要手动复制粘贴不知道要花多久，所以就用python自动化一下。
## v1

整个过程分三步

### 1.拆分为以缩写命名的单个文件

### 2.将同一物种的序列归类，放入以物种命名的文件夹

### 3.发现txt文件中的缩写与物种名表格的缩写部分不相同，暂时处理：找出无法匹配的缩写单独放入一个文件夹，人工处理

