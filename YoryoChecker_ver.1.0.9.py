import wx
import os
import threading
import pyperclip
import time
# import pprint

input_child_paths = []
input_parent_paths = []

# チェック階層選択用の関数
def buttonInputChildPath(event):
    if event.GetId() == 1111:
        default_dir = '/Users/' 
        
        # フォルダ選択ダイアログを作成
        dialog = wx.DirDialog(None, u'チェックする月の階層を入力して下さい')   
        # ファイル選択ダイアログを表示
        dialog.ShowModal()
        # フォルダのパスを取得
        input_child_path = dialog.GetPath()
        
        # 新しく選んだら既に入っているテキストを消し、動画のパスを入力
        if input_child_path:
            input_child_path_box.Clear()
            input_child_path_box.SetValue(input_child_path)

        # 古いパス情報は消した上で、リストとして次の関数に渡す
        input_child_paths.clear()
        input_child_paths.append(input_child_path)
        # print(input_child_path)

# まずは１階層分取得
def buttonCheckSize(event):
    if event.GetId() == 3333:

        input_child_path = input_child_paths[0]

        # ディレクトリ名のみの一覧を取得
        files = os.listdir(input_child_path)
        

        # 容量を把握する関数を定義
        def get_dir_size(path='.'):
            child_total = 0
            with os.scandir(path) as it:
                # is_file(), is_dir()メソッドでファイルかディレクトリかを判定
                for entry in it:
                    # ファイルの場合はstat_resultオブジェクトのst_size属性でサイズを取得
                    if entry.is_file():
                        child_total += entry.stat().st_size
                    # ディレクトリの場合はこの関数を再帰的に呼び出して、すべてのサイズを加算し合計サイズを返している。
                    elif entry.is_dir():
                        child_total += get_dir_size(entry.path)
            return child_total

        # 「パス:容量」の辞書を作る
        dirs_dict = {}

        # 「パス:容量」の辞書の要素１つ分を作る
        def makingDict(dir):
            if os.path.isdir(os.path.join(input_child_path, dir)):
                dir = input_child_path + '/' + dir
                dirs_dict[dir] = get_dir_size(dir)   

        # スレッドを使って容量を計測する
        for dir in files:
            t = threading.Thread(target=makingDict(dir))
            t.start()
            # print(threading.active_count())
            t.join()
            # 漏れをなくすため意図的にスピードを落としてやる必要があるかも
            if threading.active_count() == 2:
                time.sleep(1)


        # 容量の大きい順に並び替え、各要素はタプルになる
        dirs_dict_sorted = sorted(dirs_dict.items(), key=lambda x:x[1], reverse=True)


        # タプルをリスト化した上で出力用のリストに入れる
        dirs_dict_sorted_list = [list(dir_dict_sorted) for dir_dict_sorted in dirs_dict_sorted]
        
        # 重いフォルダベスト10を記入する関数
        changeResultText(dirs_dict_sorted_list)

# 重いフォルダベスト10を記入する関数
def changeResultText(dirs_dict_sorted_list):
    # 既に入っているテキストをクリア
    check_result_text01.Clear()
    check_result_text02.Clear()
    check_result_text03.Clear()
    check_result_text04.Clear()
    check_result_text05.Clear()
    check_result_text06.Clear()
    check_result_text07.Clear()
    check_result_text08.Clear()
    check_result_text09.Clear()
    check_result_text10.Clear()
    
    # パス、容量、パーセントを記入
    check_result_text01.SetValue(f'{dirs_dict_sorted_list[0][0]}:::::{round(dirs_dict_sorted_list[0][1] / (1000 ** 3), 2)}GB')   
    check_result_text02.SetValue(f'{dirs_dict_sorted_list[1][0]}:::::{round(dirs_dict_sorted_list[1][1] / (1000 ** 3), 2)}GB')
    check_result_text03.SetValue(f'{dirs_dict_sorted_list[2][0]}:::::{round(dirs_dict_sorted_list[2][1] / (1000 ** 3), 2)}GB')
    check_result_text04.SetValue(f'{dirs_dict_sorted_list[3][0]}:::::{round(dirs_dict_sorted_list[3][1] / (1000 ** 3), 2)}GB')
    check_result_text05.SetValue(f'{dirs_dict_sorted_list[4][0]}:::::{round(dirs_dict_sorted_list[4][1] / (1000 ** 3), 2)}GB')
    check_result_text06.SetValue(f'{dirs_dict_sorted_list[5][0]}:::::{round(dirs_dict_sorted_list[5][1] / (1000 ** 3), 2)}GB')
    check_result_text07.SetValue(f'{dirs_dict_sorted_list[6][0]}:::::{round(dirs_dict_sorted_list[6][1] / (1000 ** 3), 2)}GB')
    check_result_text08.SetValue(f'{dirs_dict_sorted_list[7][0]}:::::{round(dirs_dict_sorted_list[7][1] / (1000 ** 3), 2)}GB')
    check_result_text09.SetValue(f'{dirs_dict_sorted_list[8][0]}:::::{round(dirs_dict_sorted_list[8][1] / (1000 ** 3), 2)}GB')
    check_result_text10.SetValue(f'{dirs_dict_sorted_list[9][0]}:::::{round(dirs_dict_sorted_list[9][1] / (1000 ** 3), 2)}GB')

# テキストをコピーする関数
def buttonCopyClick(event):
    if event.GetId() == 4444:

        # テキストを取得
        get_text01 = check_result_text01.GetValue()
        get_text02 = check_result_text02.GetValue()
        get_text03 = check_result_text03.GetValue()
        get_text04 = check_result_text04.GetValue()
        get_text05 = check_result_text05.GetValue()
        get_text06 = check_result_text06.GetValue()
        get_text07 = check_result_text07.GetValue()
        get_text08 = check_result_text08.GetValue()
        get_text09 = check_result_text09.GetValue()
        get_text10 = check_result_text10.GetValue()
        
        # テキストをまとめる
        get_text_all = get_text01 + '\n' + get_text02 + '\n' + get_text03 + '\n' +get_text04 + '\n' + get_text05 + '\n' +get_text06 + '\n' +get_text07 + '\n' +get_text08 + '\n' + get_text09 + '\n' +get_text10

        # print(get_text_all)

        # クリップボードへコピー
        pyperclip.copy(get_text_all)

# ==============================================================================


application = wx.App()
 
frame = wx.Frame(None, wx.ID_ANY, '容量チェッカー', size=(1400, 550))

# Panelをテキストやボタンなどを配置するために使用
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour('#e6aa15')

# 子階層入力を促すテキスト
input_child_text = wx.StaticText(panel, wx.ID_ANY, '↓チェックする月の階層を入力して下さい', pos=(15,15))
# # フォントを指定
input_child_text_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
input_child_text.SetFont(input_child_text_font)

# 子階層パス入力欄
input_child_path_box = wx.TextCtrl(panel, wx.ID_ANY, pos=(15,35), size=(900,25))

# 子階層パス入力ボタン
button_child_input = wx.Button(panel, 1111, 'パスを入力', pos=(930,36))
button_child_input.Bind(wx.EVT_BUTTON, buttonInputChildPath)

# チェック実行ボタン
button_check = wx.Button(panel, 3333, 'チェック実行！', pos=(1020,36))
button_check.Bind(wx.EVT_BUTTON, buttonCheckSize)

# 番号のテキスト
number_text01 = wx.StaticText(panel, wx.ID_ANY, '01,', pos=(15,135))
number_text02 = wx.StaticText(panel, wx.ID_ANY, '02,', pos=(15,165))
number_text03 = wx.StaticText(panel, wx.ID_ANY, '03,', pos=(15,195))
number_text04 = wx.StaticText(panel, wx.ID_ANY, '04,', pos=(15,225))
number_text05 = wx.StaticText(panel, wx.ID_ANY, '05,', pos=(15,255))
number_text06 = wx.StaticText(panel, wx.ID_ANY, '06,', pos=(15,285))
number_text07 = wx.StaticText(panel, wx.ID_ANY, '07,', pos=(15,315))
number_text08 = wx.StaticText(panel, wx.ID_ANY, '08,', pos=(15,345))
number_text09 = wx.StaticText(panel, wx.ID_ANY, '09,', pos=(15,375))
number_text10 = wx.StaticText(panel, wx.ID_ANY, '10,', pos=(15,405))

# 番号のテキストのフォントを指定
number_text_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
number_text01.SetFont(number_text_font)
number_text02.SetFont(number_text_font)
number_text03.SetFont(number_text_font)
number_text04.SetFont(number_text_font)
number_text05.SetFont(number_text_font)
number_text06.SetFont(number_text_font)
number_text07.SetFont(number_text_font)
number_text08.SetFont(number_text_font)
number_text09.SetFont(number_text_font)
number_text10.SetFont(number_text_font)

# チェック結果を表示するテキスト
check_result_text00 = wx.StaticText(panel, wx.ID_ANY, '容量の大きいものから順に……', pos=(15,105))
check_result_text01 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,135), size=(1300,25))
check_result_text02 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,165), size=(1300,25))
check_result_text03 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,195), size=(1300,25))
check_result_text04 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,225), size=(1300,25))
check_result_text05 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,255), size=(1300,25))
check_result_text06 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,285), size=(1300,25))
check_result_text07 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,315), size=(1300,25))
check_result_text08 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,345), size=(1300,25))
check_result_text09 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,375), size=(1300,25))
check_result_text10 = wx.TextCtrl(panel, wx.ID_ANY, '', pos=(45,405), size=(1300,25))

# check_result_text系のフォントを指定
check_result_textfont = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

check_result_text00.SetFont(check_result_textfont)
check_result_text01.SetFont(check_result_textfont)
check_result_text02.SetFont(check_result_textfont)
check_result_text03.SetFont(check_result_textfont)
check_result_text04.SetFont(check_result_textfont)
check_result_text05.SetFont(check_result_textfont)
check_result_text06.SetFont(check_result_textfont)
check_result_text07.SetFont(check_result_textfont)
check_result_text08.SetFont(check_result_textfont)
check_result_text09.SetFont(check_result_textfont)
check_result_text10.SetFont(check_result_textfont)

# コピーボタン
button_copy = wx.Button(panel, 4444, '結果をコピー', pos=(1250,450))
# 後でコピー用の関数を作るzzzzzz↓
button_copy.Bind(wx.EVT_BUTTON, buttonCopyClick)

# 中央へ表示する
frame.Centre()
frame.Show()
 
application.MainLoop()