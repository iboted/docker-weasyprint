from weasyprint import CSS
from weasyprint.text.fonts import FontConfiguration

def css_for_extra_fonts():
    font_config = FontConfiguration()
    return CSS(string='''
        @font-face {
            font-family: 'BC Sans Regular';
            src: local('BCSans-Regular');
        }
        @font-face {
            font-family: 'BC Sans Bold';
            src: local('BCSans-Bold');
        }
        @font-face {
            font-family: 'BC Sans Bold Italic';
            src: local('BCSans-BoldItalic');
        }
        @font-face {
            font-family: 'BC Sans Italic';
            src: local('BCSans-Italic');
        }
        @font-face {
            font-family: 'Noto Sans Light';
            src: local('NotoSans-Light');
        }
        @font-face {
            font-family: 'Noto Sans Light Italic';
            src: local('NotoSans-LightItalic');
        }
        @font-face {
          font-family: Gunplay;
          src: url(gunplayrg.ttf);
        }
        @font-face {
          font-family: Source Sans Pro;
          font-weight: 400;
          src: url(sourcesanspro-regular.otf);
        }
        @font-face {
          font-family: Source Sans Pro;
          font-weight: 700;
          src: url(sourcesanspro-bold.otf);
        }
        ''', font_config=font_config), font_config
