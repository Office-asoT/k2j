import unittest

from k2j import k2j


class TestK2J(unittest.TestCase):
    def test_k2j(self):
        test_cases = [
            # 参考: http://slp.itc.nagoya-u.ac.jp/web/papers/2007/hayashi_SLP66.pdf
            ('今日はいい天気です', '今日はいい天気である'),
            ('リストにはさまざまな訴えが並びます。', 'リストにはさまざまな訴えが並ぶ。'),
            ('政府筋が31日、明らかにしました。', '政府筋が31日、明らかにした。'),
            ('銃弾は見つかっていません。', '銃弾は見つかっていない。'),
            ('脅威に思った関係者はほとんどいませんでした。', '脅威に思った関係者はほとんどいなかった。'),
            ('国民に応えていかなければならない課題です。', '国民に応えていかなければならない課題である。'),
            ('マンネリズムを見事に打破したものでした。', 'マンネリズムを見事に打破したものだった。'),
            ('党内にそれほどの動揺はありません。', '党内にそれほどの動揺はない。'),
            ('他の追従を許さないところです。', '他の追従を許さないところである。'),
            ('独自の作風を打ち立てたのでした。', '独自の作風を打ち立てたのであった。'),
            ('自由な世界がくると信じたからでしょう。', '自由な世界がくると信じたからであろう。'),
            ('決して楽な戦いではないでしょう。', '決して楽な戦いではないだろう。'),
            ('ですが、実質所得は激減しています。', 'だが、実質所得は激減している。'),
            ('高利と分かっていてもほかに選択肢がありません。', '高利と分かっていてもほかに選択肢がない。'),
            ('後続の運行に支障はありませんでした。', '後続の運行に支障はなかった。'),
            # 以下、k2j オリジナルのテストケース
            ('以下の方法で使用されます。', '以下の方法で使用される。'),
            ('以下の方法で使用されました。', '以下の方法で使用された。'),
            ('この公約は多くの人から支持されません。', 'この公約は多くの人から支持されない。'),
            ('この公約は多くの人から支持されませんでした。', 'この公約は多くの人から支持されなかった。'),
            ('図~\\ref{{fig:model}} に示すように、このモデルは 4 つの要素から構成されます。', '図~\\ref{{fig:model}} に示すように、このモデルは 4 つの要素から構成される。'),
            ('一般的なサイズよりも遥かに大きいです。', '一般的なサイズよりも遥かに大きい。'),
            ('欠点は少なかったです。', '欠点は少なかった。'),
            ('絵を描きました。', '絵を描いた。'),
            ('大学で教育学を学びました。', '大学で教育学を学んだ。'),
            ('本研究では調査を行いました。', '本研究では調査を行った。'),
            ('良い結果が得られました。', '良い結果が得られた。')
        ]
        for input_text, expected_output in test_cases:
            with self.subTest(input_text=input_text, expected_output=expected_output):
                self.assertEqual(k2j(input_text), expected_output)


if __name__ == '__main__':
    unittest.main()
