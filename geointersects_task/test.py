#!/usr/bin/python3

def test_file_exists(s):
    cmd = 'test -f /home/box/answer'
    assert s.run(cmd).succeeded, "File not found"

def test_file_content(s):
    correct_answer = '[135.26, 67.07], [132.45, 61.02], [138.25, 62.63], [145.11, 67.20], [135.26, 67.07]'
    user_answer = s.run('cat /home/box/answer')

    assert user_answer == correct_answer, "Ваш ответ не совпадает с правильным."
