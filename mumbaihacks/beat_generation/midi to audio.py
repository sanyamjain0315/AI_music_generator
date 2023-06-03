import mido
import fluidsynth

def convert_midi_to_audio(midi_file, soundfont_file, output_audio_file):
    # Create a FluidSynth instance
    fs = fluidsynth.Synth()

    # Load the soundfont file
    sfid = fs.sfload(soundfont_file)

    # Start the FluidSynth audio driver
    fs.start(driver='alsa')

    # Load the MIDI file
    mid = mido.MidiFile(midi_file)

    # Iterate over MIDI tracks and events
    for msg in mid.play():
        # Convert MIDI messages to FluidSynth format and send to the synthesizer
        fs.write(msg)

    # Stop the audio driver
    fs.stop()

    # Save the generated audio to a WAV file
    fs.wavewrite(output_audio_file)

    # Clean up resources
    fs.delete()

# Usage example
midi_file = 'input.mid'
soundfont_file = 'soundfont.sf2'
output_audio_file = 'output.wav'

convert_midi_to_audio(midi_file, soundfont_file, output_audio_file)
