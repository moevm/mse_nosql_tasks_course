#!/usr/bin/python3
# -*- coding: utf-8 -*-

def test_index(s):  #what is s?
    result = s.run('mongo my_db --eval \'db.places.getIndexes()\' 2>/dev/null | grep -q loc_2dsphere')
    assert result.succeeded, "Ваш ответ не совпадает с правильным"