def jaccard(x, y):
    """
    jaccard similarity function
    集合XとYの共通要素数を少なくとも１方にある要素の総数で割ったもの

    j(x, y) = |x & y| / |x | y|

    param x , y : text
    return : jaccard similarity
    """
    import MeCab
    t = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    _x = list(t.parse(x).split(' '))
    _x.remove('\n')
    _x = set(_x)
    _y = t.parse(y).split(' ')
    _y.remove('\n')
    _y = set(_y)

    result = len(_x & _y) / len(_x | _y)
    print('|X & Y| : {}'.format(len(_x & _y)))
    print('|X | Y| : {}'.format(len(_x | _y)))

    return result

def dice(x, y):
    """
    dice similarity function
    集合XとYの共通要素数を各集合の要素数の平均で割ったもの

    j(x, y) = 2 * |x & y| / ||x|+|y||

    param x , y : text
    return : dice similarity
    """
    import MeCab
    t = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    _x = list(t.parse(x).split(' '))
    _x.remove('\n')
    _x = set(_x)
    _y = t.parse(y).split(' ')
    _y.remove('\n')
    _y = set(_y)
          
    result = 2 * len(_x & _y) / sum(map(len, (_x, _y)))
    print('2 * |X & Y| : {}'.format(2 * len(_x & _y)))
    print('|X|+|Y| : {}'.format(sum(map(len, (_x, _y)))))

    return result

def simpson(x, y):
    """
    simpson similarity function


    j(x, y) = |x & y| / min||x|+|y||

    param x , y : text
    return : simpson similarity
    """
    import MeCab
    t = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    _x = list(t.parse(x).split(' '))
    _x.remove('\n')
    _x = set(_x)
    _y = t.parse(y).split(' ')
    _y.remove('\n')
    _y = set(_y)
          
    result = len(_x & _y) / min(map(len, (_x, _y)))
    print('|X & Y| : {}'.format(len(_x & _y)))
    print('min(|X|,|Y|) : {}'.format(min(map(len, (_x, _y)))))

    return result


if __name__ == '__main__':
    text1 = "山田さんは綺麗です。"
    text2 = "山と田んぼは綺麗です。"
    print("text1 : {}".format(text1))
    print("text2 : {}".format(text2))
    print("")
    print("jaccard : {}".format(jaccard(text1, text2)))
    print("")
    print("dice : {}".format(dice(text1, text2)))
    print("")
    print("simpson : {}".format(simpson(text1, text2)))
