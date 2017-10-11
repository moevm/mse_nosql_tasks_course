def test_file_exists(s):
    cmd = 'test -f /home/box/answer'
    assert s.run(cmd).succeeded, "File not found"


def test_file_content(s):
    correct_answer = '0.27769'
    user_answer = s.run('cat /home/box/answer')

    assert user_answer == correct_answer, "Ваш ответ не совпадает с правильным."
