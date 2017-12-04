from flask_script import Command
from models import Stage, TeamResult


class Seed(Command):
    def stage_import(self):
        stages = [{'id': '2',
                  'image': '/images/stage/187987856bf575c4155d021cb511034931d06d24.png',
                  'name': 'ガンガゼ野外音楽堂'},
                 {'id': '1',
                  'image': '/images/stage/83acec875a5bb19418d7b87d5df4ba1e38ceac66.png',
                  'name': 'フジツボスポーツクラブ'},
                 {'id': '5',
                  'image': '/images/stage/fc23fedca2dfbbd8707a14606d719a4004403d13.png',
                  'name': 'コンブトラック'},
                 {'id': '11',
                  'image': '/images/stage/758338859615898a59e93b84f7e1ca670f75e865.png',
                  'name': 'Ｂバスパーク'},
                 {'id': '3',
                  'image': '/images/stage/bc794e337900afd763f8a88359f83df5679ddf12.png',
                  'name': 'チョウザメ造船'},
                 {'id': '7',
                  'image': '/images/stage/0907fc7dc325836a94d385919fe01dc13848612a.png',
                  'name': 'ホッケふ頭'},
                 {'id': '6',
                  'image': '/images/stage/070d7ee287fdf3c5df02411950c2a1ce5b238746.png',
                  'name': 'マンタマリア号'},
                 {'id': '13',
                  'image': '/images/stage/d9f0f6c330aaa3b975e572637b00c4c0b6b89f7d.png',
                  'name': 'ザトウマーケット'},
                 {'id': '10',
                  'image': '/images/stage/a12e4bf9f871677a5f3735d421317fbbf09e1a78.png',
                  'name': 'モズク農園'},
                 {'id': '0',
                  'image': '/images/stage/98baf21c0366ce6e03299e2326fe6d27a7582dce.png',
                  'name': 'バッテラストリート'}]

        for stage in stages:
            Stage.save_from_dict(stage)

    def rule_import(self):
        pass

    def game_mode_import(self):
        pass

    def team_result_import(self):
        TeamResult(id=1, key='victory', name='WIN!').add().commit()
        TeamResult(id=2, key='defeat', name='LOSE...').add().commit()

    def run(self):
        self.stage_import()
        self.team_result_import()
