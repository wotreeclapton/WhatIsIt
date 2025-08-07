'''
WHAT IS IT APP LAUNCHER - Entry point
	Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

from what_is_it.main import Main_Gui
import what_is_it.constants as const


Main_Gui()

if __name__ == "__main__":
	print("Author:", const.__author__)
	print("App version:",const.__version__)

	Main_Gui()