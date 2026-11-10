import subprocess
import sys

from sandbox.cli import main


def test_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from sandbox!\n"


def test_cli_module():
    result = subprocess.run(
        [sys.executable, "-m", "sandbox"],
        capture_output=True,  # 標準出力と標準エラーをキャプチャ
        text=True,  # 出力をバイト列ではなく文字列（str）として取得
        check=True,
    )
    # 期待する標準出力（stdout）の検証（末尾の改行コードに注意）
    assert "Hello from sandbox!" in result.stdout
    # 必要に応じて終了ステータス（0は正常終了）も検証
    assert result.returncode == 0


def test_cli_script():
    result = subprocess.run(
        "sandbox",
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Hello from sandbox!" in result.stdout
    assert result.returncode == 0
