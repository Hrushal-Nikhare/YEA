import words
import struct

def get_simple_insult(target_noun):
    return f"{target_noun} is {words.get_insulting_adjective()}"
def get_so_insult(target_noun):
    return "%s's so %s"%(target_noun, words.get_insulting_adjective())
def get_so_insult_with_action(target_noun, target_pronoun):
    return "%s's so %s, %s %s"%(target_noun, words.get_insulting_adjective(), target_pronoun, words.get_past_tense_verb())
def get_so_insult_with_action_and_target(target_noun, target_pronoun):
    return "%s's so %s, %s %s the %s"%(target_noun, words.get_insulting_adjective(), target_pronoun, words.get_past_tense_verb(), words.get_noun())
