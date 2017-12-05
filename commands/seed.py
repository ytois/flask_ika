from flask_script import Command
from models import db, Stage, TeamResult, Rule, GameMode


class Seed(Command):
    def stage_import(self):
        stages = [
            {'id': '0',
             'image': '/images/stage/98baf21c0366ce6e03299e2326fe6d27a7582dce.png',
             'name': 'バッテラストリート'},
            {'id': '1',
             'image': '/images/stage/83acec875a5bb19418d7b87d5df4ba1e38ceac66.png',
             'name': 'フジツボスポーツクラブ'},
            {'id': '2',
             'image': '/images/stage/187987856bf575c4155d021cb511034931d06d24.png',
             'name': 'ガンガゼ野外音楽堂'},
            {'id': '3',
             'image': '/images/stage/bc794e337900afd763f8a88359f83df5679ddf12.png',
             'name': 'チョウザメ造船'},
            {'id': '4',
             'image': '/images/stage/5c030a505ee57c889d3e5268a4b10c1f1f37880a.png',
             'name': '海女美術大学'},
            {'id': '5',
             'image': '/images/stage/fc23fedca2dfbbd8707a14606d719a4004403d13.png',
             'name': 'コンブトラック'},
            {'id': '6',
             'image': '/images/stage/070d7ee287fdf3c5df02411950c2a1ce5b238746.png',
             'name': 'マンタマリア号'},
            {'id': '7',
             'image': '/images/stage/0907fc7dc325836a94d385919fe01dc13848612a.png',
             'name': 'ホッケふ頭'},
            {'id': '8',
             'image': '/images/stage/96fd8c0492331a30e60a217c94fd1d4c73a966cc.png',
             'name': 'タチウオパーキング'},
            {'id': '9',
             'image': '/images/stage/8c95053b3043e163cbfaaf1ec1e5f3eb770e5e07.png',
             'name': 'エンガワ河川敷'},
            {'id': '10',
             'image': '/images/stage/a12e4bf9f871677a5f3735d421317fbbf09e1a78.png',
             'name': 'モズク農園'},
            {'id': '11',
             'image': '/images/stage/758338859615898a59e93b84f7e1ca670f75e865.png',
             'name': 'Ｂバスパーク'},
            {'id': '13',
             'image': '/images/stage/d9f0f6c330aaa3b975e572637b00c4c0b6b89f7d.png',
             'name': 'ザトウマーケット'},
        ]

        for stage in stages:
            Stage.save_from_dict(stage)

    def rule_import(self):
        rules = [
            Rule(id=1, name='ナワバリバトル', name_en='turf_war'),
            Rule(id=2, name='ガチエリア', name_en='splat_zones'),
            Rule(id=3, name='ガチヤグラ', name_en='tower_control'),
            Rule(id=4, name='ガチホコ', name_en='rainmaker'),
            # Rule(id=5, name='ガチアサリ', name_en='')
        ]

        db.session.query(Rule).delete()
        db.session.add_all(rules)
        db.session.commit()

    def game_mode_import(self):
        game_modes = [
            GameMode(id=1, name='レギュラーマッチ', name_en='regular'),
            GameMode(id=2, name='ガチマッチ', name_en='gachi'),
            GameMode(id=3, name='リーグマッチ', name_en='league'),
            GameMode(id=4, name='プライベートマッチ', name_en='priovate'),
        ]

        db.session.query(GameMode).delete()
        db.session.add_all(game_modes)
        db.session.commit()

    def team_result_import(self):
        db.session.query(TeamResult).delete()
        db.session.add_all([
            TeamResult(id=1, key='victory', name='WIN!'),
            TeamResult(id=2, key='defeat', name='LOSE...')
        ])
        db.session.commit()

    def run(self):
        self.stage_import()
        self.team_result_import()
        self.game_mode_import()
        self.rule_import()
