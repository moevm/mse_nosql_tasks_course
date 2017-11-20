#!/usr/bin/python3
# -*- coding: utf-8 -*-

def test_index(s):  
    result = s.run('mongo my_db --eval \'db.places.getIndexes()\' 2>/dev/null | grep -q location_2dsphere')
    assert result.succeeded, "Ваш ответ не совпадает с правильным"