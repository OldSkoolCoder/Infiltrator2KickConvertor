# Infiltrator Conversion Utilities

Three utilities to help convert the Infiltrator files into more usable and readable ASM Files For : 
* Kick 
* CBM PRg Studio (CPS)

## Kick Conversion Files
### ConvertCSFileToASM.py
This file will take the binary file created by Infiltrator and convert it into readable assembly Kick formated file 
E.g.
```	// Character Number : 0  HexOffset : $0000 
	.byte %00011100			// ...xxx..
	.byte %00100010			// ..x...x.
	.byte %01001010			// .x..x.x.
	.byte %01010110			// .x.x.xx.
	.byte %01001100			// .x..xx..
	.byte %00100000			// ..x.....
	.byte %00011110			// ...xxxx.
	.byte %00000000			// ........


	// Character Number : 1  HexOffset : $0008 
	.byte %11110000			// xxxx....
	.byte %10001000			// x...x...
	.byte %10000100			// x....x..
	.byte %11111110			// xxxxxxx.
	.byte %10000010			// x.....x.
	.byte %10000010			// x.....x.
	.byte %10000010			// x.....x.
	.byte %00000000			// ........
```

#### How to use
in command box or terminal type :

**python3 ConvertCSFileToASM.py --input=Filename --output=Filename**

* *--input* is the input binary file to convert.
* *--output* is the output assembly text file of the conversion.

### ConvertSPRFileToASM.py
This file will take the binary file created by Infiltrator and convert it into readable assembly Kick formated file 
E.g.
```	// Sprite Number : 0  HexOffset : $0000 
	.byte %00010000, %00000000, %00010010		// ...x.... ........ ...x..x.
	.byte %00001000, %01111110, %00011100		// ....x... .xxxxxx. ...xxx..
	.byte %00000101, %11111111, %11001100		// .....x.x xxxxxxxx xx..xx..
	.byte %00000110, %00010000, %00110110		// .....xx. ...x.... ..xx.xx.
	.byte %00001111, %10011111, %11110000		// ....xxxx x..xxxxx xxxx....
	.byte %00001000, %10010010, %00010000		// ....x... x..x..x. ...x....
	.byte %00001000, %11110011, %11110000		// ....x... xxxx..xx xxxx....
	.byte %00001000, %11110010, %00010000		// ....x... xxxx..x. ...x....
	.byte %00001000, %11110100, %00001000		// ....x... xxxx.x.. ....x...
	.byte %00011111, %11111110, %00011000		// ...xxxxx xxxxxxx. ...xx...
	.byte %00100000, %00000001, %11110100		// ..x..... .......x xxxx.x..
	.byte %00100000, %00000000, %10100100		// ..x..... ........ x.x..x..
	.byte %00100111, %10000000, %10111100		// ..x..xxx x....... x.xxxx..
	.byte %00100111, %11000000, %10100100		// ..x..xxx xx...... x.x..x..
	.byte %00011111, %11111111, %11111100		// ...xxxxx xxxxxxxx xxxxxx..
	.byte %00001101, %00111100, %10110000		// ....xx.x ..xxxx.. x.xx....
	.byte %00011001, %11000011, %10011000		// ...xx..x xx....xx x..xx...
	.byte %00110001, %00000000, %10001100		// ..xx...x ........ x...xx..
	.byte %00110000, %00000000, %00001100		// ..xx.... ........ ....xx..
	.byte %01111000, %00000000, %00011110		// .xxxx... ........ ...xxxx.
	.byte %11001100, %11111111, %00110011		// xx..xx.. ........ ..xx..xx
	.byte %00000000								// ........
```

### How to use
in command box or terminal type :

**python3 ConvertSPRFileToASM.py --input=Filename --output=Filename**

* *--input* is the input binary file to convert.
* *--output* is the output assembly text file of the conversion.

### ConvertINFILTRATORFileToASM.py
This file will take the disassembly text file created by Infiltrator and convert it into readable assembly Kick formated file 

**E.g. Before**
```//------------------------------
L_JSR_($8022)_($0967) OK
L_JSR_($8022)_($80C5) OK
//------------------------------
$8022  A9 04     LDA #$04
$8024  85 49     STA $49 
$8026  A9 00     LDA #$00
$8028  85 48     STA $48 
$802A  A2 00     LDX #$00
//------------------------------
L_BRS_($802C)_($8046) OK
//------------------------------
$802C  A5 48     LDA $48 
$802E  9D 40 03  STA $0340,X 
$8031  A5 49     LDA $49 
$8033  9D 60 03  STA $0360,X 
$8036  A5 48     LDA $48 
$8038  18        CLC 
$8039  69 28     ADC #$28
$803B  85 48     STA $48 
$803D  A5 49     LDA $49 
$803F  69 00     ADC #$00
$8041  85 49     STA $49 
$8043  E8        INX 
$8044  E0 18     CPX #$18
$8046  D0 E4     BNE L_BRS_($802C)_($8046) OK
$8048  60        RTS 
//------------------------------
L_JSR_($8049)_($08FA) OK
L_JSR_($8049)_($0900) OK
L_JSR_($8049)_($1549) OK
L_JSR_($8049)_($1C1C) OK
L_JSR_($8049)_($1C3C) OK
L_JSR_($8049)_($8058) OK
L_JSR_($8049)_($805E) OK
L_JSR_($8049)_($8CC1) OK
L_JSR_($8049)_($93AC) OK
L_JSR_($8049)_($93CC) OK
//------------------------------
$8049  A6 03     LDX $03 
$804B  A4 02     LDY $02 
$804D  BD 40 03  LDA $0340,X 
$8050  85 48     STA $48 
$8052  BD 60 03  LDA $0360,X 
$8055  85 49     STA $49 
$8057  60        RTS 
```

**E.g. After**
```//------------------------------
L_JSR_8022_0967_OK:
L_JSR_8022_80C5_OK:
//------------------------------
	lda #$04
	sta $49 
	lda #$00
	sta $48 
	ldx #$00
//------------------------------
L_BRS_802C_8046_OK:
//------------------------------
	lda $48 
	sta $0340,X 
	lda $49 
	sta $0360,X 
	lda $48 
	clc 
	adc #$28
	sta $48 
	lda $49 
	adc #$00
	sta $49 
	inx 
	cpx #$18
	bne L_BRS_802C_8046_OK
	rts 
//------------------------------
L_JSR_8049_08FA_OK:
L_JSR_8049_0900_OK:
L_JSR_8049_1549_OK:
L_JSR_8049_1C1C_OK:
L_JSR_8049_1C3C_OK:
L_JSR_8049_8058_OK:
L_JSR_8049_805E_OK:
L_JSR_8049_8CC1_OK:
L_JSR_8049_93AC_OK:
L_JSR_8049_93CC_OK:
//------------------------------
	ldx $03 
	ldy $02 
	lda $0340,X 
	sta $48 
	lda $0360,X 
	sta $49 
	rts 
```

### How to use
in command box or terminal type :

**python3 ConvertINFILTRATORFileToASM.py --input=Filename --output=Filename**

* *--input* is the input text dissassembly file to convert.
* *--output* is the output assembly text file of the conversion.

## CBM Prg Studio (CPS) Conversion Files
### ConvertCSFileToCPSASM.py
This file will take the binary file created by Infiltrator and convert it into readable assembly CPS formated file 
E.g.
```	; Character Number : 0  HexOffset : $0000 
	byte %00011100			; ...xxx..
	byte %00100010			; ..x...x.
	byte %01001010			; .x..x.x.
	byte %01010110			; .x.x.xx.
	byte %01001100			; .x..xx..
	byte %00100000			; ..x.....
	byte %00011110			; ...xxxx.
	byte %00000000			; ........


	; Character Number : 1  HexOffset : $0008 
	byte %11110000			; xxxx....
	byte %10001000			; x...x...
	byte %10000100			; x....x..
	byte %11111110			; xxxxxxx.
	byte %10000010			; x.....x.
	byte %10000010			; x.....x.
	byte %10000010			; x.....x.
	byte %00000000			; ........
```

#### How to use
in command box or terminal type :

**python3 ConvertCSFileToCPSASM.py --input=Filename --output=Filename**

* *--input* is the input binary file to convert.
* *--output* is the output assembly text file of the conversion.

### ConvertSPRFileToASM.py
This file will take the binary file created by Infiltrator and convert it into readable assembly CPS formatted file 
E.g.
```	; Sprite Number : 0  HexOffset : $0000 
	byte %00010000, %00000000, %00010010		; ...x.... ........ ...x..x.
	byte %00001000, %01111110, %00011100		; ....x... .xxxxxx. ...xxx..
	byte %00000101, %11111111, %11001100		; .....x.x xxxxxxxx xx..xx..
	byte %00000110, %00010000, %00110110		; .....xx. ...x.... ..xx.xx.
	byte %00001111, %10011111, %11110000		; ....xxxx x..xxxxx xxxx....
	byte %00001000, %10010010, %00010000		; ....x... x..x..x. ...x....
	byte %00001000, %11110011, %11110000		; ....x... xxxx..xx xxxx....
	byte %00001000, %11110010, %00010000		; ....x... xxxx..x. ...x....
	byte %00001000, %11110100, %00001000		; ....x... xxxx.x.. ....x...
	byte %00011111, %11111110, %00011000		; ...xxxxx xxxxxxx. ...xx...
	byte %00100000, %00000001, %11110100		; ..x..... .......x xxxx.x..
	byte %00100000, %00000000, %10100100		; ..x..... ........ x.x..x..
	byte %00100111, %10000000, %10111100		; ..x..xxx x....... x.xxxx..
	byte %00100111, %11000000, %10100100		; ..x..xxx xx...... x.x..x..
	byte %00011111, %11111111, %11111100		; ...xxxxx xxxxxxxx xxxxxx..
	byte %00001101, %00111100, %10110000		; ....xx.x ..xxxx.. x.xx....
	byte %00011001, %11000011, %10011000		; ...xx..x xx....xx x..xx...
	byte %00110001, %00000000, %10001100		; ..xx...x ........ x...xx..
	byte %00110000, %00000000, %00001100		; ..xx.... ........ ....xx..
	byte %01111000, %00000000, %00011110		; .xxxx... ........ ...xxxx.
	byte %11001100, %11111111, %00110011		; xx..xx.. ........ ..xx..xx
	byte %00000000								; ........
```

### How to use
in command box or terminal type :

**python3 ConvertSPRFileToCPSASM.py --input=Filename --output=Filename**

* *--input* is the input binary file to convert.
* *--output* is the output assembly text file of the conversion.

### ConvertINFILTRATORFileToASM.py
This file will take the disassembly text file created by Infiltrator and convert it into readable assembly KCPSick formatted file 

**E.g. Before**
```//------------------------------
L_JSR_($8022)_($0967) OK
L_JSR_($8022)_($80C5) OK
//------------------------------
$8022  A9 04     LDA #$04
$8024  85 49     STA $49 
$8026  A9 00     LDA #$00
$8028  85 48     STA $48 
$802A  A2 00     LDX #$00
//------------------------------
L_BRS_($802C)_($8046) OK
//------------------------------
$802C  A5 48     LDA $48 
$802E  9D 40 03  STA $0340,X 
$8031  A5 49     LDA $49 
$8033  9D 60 03  STA $0360,X 
$8036  A5 48     LDA $48 
$8038  18        CLC 
$8039  69 28     ADC #$28
$803B  85 48     STA $48 
$803D  A5 49     LDA $49 
$803F  69 00     ADC #$00
$8041  85 49     STA $49 
$8043  E8        INX 
$8044  E0 18     CPX #$18
$8046  D0 E4     BNE L_BRS_($802C)_($8046) OK
$8048  60        RTS 
//------------------------------
L_JSR_($8049)_($08FA) OK
L_JSR_($8049)_($0900) OK
L_JSR_($8049)_($1549) OK
L_JSR_($8049)_($1C1C) OK
L_JSR_($8049)_($1C3C) OK
L_JSR_($8049)_($8058) OK
L_JSR_($8049)_($805E) OK
L_JSR_($8049)_($8CC1) OK
L_JSR_($8049)_($93AC) OK
L_JSR_($8049)_($93CC) OK
//------------------------------
$8049  A6 03     LDX $03 
$804B  A4 02     LDY $02 
$804D  BD 40 03  LDA $0340,X 
$8050  85 48     STA $48 
$8052  BD 60 03  LDA $0360,X 
$8055  85 49     STA $49 
$8057  60        RTS 
```

**E.g. After**
```;------------------------------
L_JSR_8022_0967_OK:
L_JSR_8022_80C5_OK:
;------------------------------
	lda #$04
	sta $49 
	lda #$00
	sta $48 
	ldx #$00
;------------------------------
L_BRS_802C_8046_OK:
;------------------------------
	lda $48 
	sta $0340,X 
	lda $49 
	sta $0360,X 
	lda $48 
	clc 
	adc #$28
	sta $48 
	lda $49 
	adc #$00
	sta $49 
	inx 
	cpx #$18
	bne L_BRS_802C_8046_OK
	rts 
;------------------------------
L_JSR_8049_08FA_OK:
L_JSR_8049_0900_OK:
L_JSR_8049_1549_OK:
L_JSR_8049_1C1C_OK:
L_JSR_8049_1C3C_OK:
L_JSR_8049_8058_OK:
L_JSR_8049_805E_OK:
L_JSR_8049_8CC1_OK:
L_JSR_8049_93AC_OK:
L_JSR_8049_93CC_OK:
;------------------------------
	ldx $03 
	ldy $02 
	lda $0340,X 
	sta $48 
	lda $0360,X 
	sta $49 
	rts 
```

### How to use
in command box or terminal type :

**python3 ConvertINFILTRATORFileToCPSASM.py --input=Filename --output=Filename**

* *--input* is the input text dissassembly file to convert.
* *--output* is the output assembly text file of the conversion.