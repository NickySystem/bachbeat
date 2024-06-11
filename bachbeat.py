import mido

pieceLen = 2056
t = 0
notes = [0] * pieceLen

print("Tempo (bpm):")
tempo1 = int(input())
tempo2 = int(60000 / int(tempo1) * 120)
print("Bytebeat Expression:")
exp = input()


def ModeFunction():
    t = 0
    print("Enter mode (wrap or squish):")
    mode = input()
    if mode == "wrap":
        for i in range(pieceLen):
            notes[i] = abs((safe_eval(exp,t)+21) % 128)
            t += 1
    elif mode == "squish":
        for t in range(pieceLen):
            notes[t] = int(abs((int((safe_eval(exp,t))+21)/255)*127))
            t += 1
    else:
        print("Error")


def safe_eval(expression, t):
    try:
        result = eval(expression)
        # Ensure the result is an integer
        result = int(result)
    except ZeroDivisionError:
        t = 1
    return result


ModeFunction()
print("File name (*.mid)")
fileN = input()


def create_midi_from_notes(note_list, filename='output.mid', bpm=tempo1):
    global tempo2, notes, fileN
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    track.append(mido.MetaMessage('set_tempo', tempo=(tempo2)))#

    for note in note_list:
        on = mido.Message('note_on', note=note, velocity=64, time=0)
        off = mido.Message('note_off', note=note, velocity=0, time=480)  # Adjust time as needed
        track.append(on)
        track.append(off)

    mid.save(filename)

create_midi_from_notes(notes, fileN)
