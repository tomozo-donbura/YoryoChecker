# YoryoChecker
This is an application to check your server capacity.

これはあなたのパソコンの中にある容量の大きいフォルダをリストアップするアプリです。

仕様
1. アプリ上で調べたい階層のフォルダを指定します

2. 1で指定した階層の下にある各フォルダの容量を調べます

3. 2の結果を元に、容量の重いフォルダトップ10のパスと容量（GiB表示）が表示されます

4. 3の結果をテキストにコピーできるようになってます。

pyperclipとwxPythonをインストールする必要があります。
wxPythonのバージョンは4.1.1 で挙動することを確認しました。

############################################

This is an application that lists large folders on your computer.

Specifications
1. specify the folders in the hierarchy to be checked on the application

2. check the capacity of each folder under the hierarchy specified in 1.

3. based on the results of 2, the paths and capacities (in GiB) of the top 10 largest folders are displayed

4. the result of 3 can be copied to text.

pyperclip and wxPython must be installed.
We have confirmed that wxPython behaves with version 4.1.1.
