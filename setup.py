import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Avoid The Ex",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":['ATEGameMap.png','ATEStartScreen.png','Chance.png','Credit2.png','Credit4.png'
,'Credit5.png','cutscene0.png','cutscene1.png','cutscene2.png','cutscene3.png','DateBig.png','DateLittle.png'
,'Ex2.png','FinalWin.png','highscore.txt','instr1.png','instr2.png','instr3.png','instrDown.png','instrLeft.png'
,'instrRight.png','instrUp.png','lvl_1.txt','lvl_2.txt','lvl_3.txt','lvl_4.txt','lvl_5.txt','lvl_6.txt','player-date1.png'
,'player-date2.png','player-date3.png','player-date4.png','Player1.png','Player2.png','Player3.png','Player4.png','slap.mp3'
,'track2.mp3','track3.mp3','Streetlight.png','YouLose.png','YouWin.png']
}},
    executables = executables

    )