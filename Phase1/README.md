# Phase I - 產生諧音梗句子

參考自[諧音梗生成器](https://mp.weixin.qq.com/s/NLqEhlMTaF1qxlDxAB2lAQ)
* Git repo: [MLab_wechat/weChat192_memeGenerator](https://github.com/DrMofu/MLab_wechat/tree/main/weChat192_memeGenerator)

## Function Interface
Input Parameter: 中文句子(str)

Output Return: 英文拼音替換部分詞語的諧音梗句子(str)和英文拼字部分(list of str)

## Usage

* 安裝套件

  ```bash
  pip install -r requirements.txt
  ```
  根據epitran[官方文件](https://pypi.org/project/epitran/)安裝`lex_lookup`		
  ```bash
  git clone https://github.com/festvox/flite.git
  cd flite/
  ./configure && make
  sudo make install
  cd testsuite
  make lex_lookup
  sudo cp lex_lookup /usr/local/bin
  ```

* 執行

  ```bash
  python3 MemeTextGenerator.py
  ```

  修改`MemeTextGenerator.py` 的main function。

* python

  ```python
  >>> from MemeTextGenerator import MemeTextGenerator
  >>> generator = MemeTextGenerator(candidates_file = 'vocabulary3000.pickle')
  >>> s = u'有備而來'
  >>> result = generator.generate(s)
  >>> print(result)
  (['有barrier來', '有備airline', '有備ally', '有備early'], ['barrier', 'airline', 'ally', 'early'])
  ```