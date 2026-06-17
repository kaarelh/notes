* pretraining on human text
* RLHF
* RLAIF
* conditional pretraining
* inoculation prompting
* prefilling bad text (eg lying) and training to correct away from it. you can do this in a supervised way where you also prefill a good correction and train on the correction tokens but not the bad tokens. or you can RLHF i guess
* just pretraining on human ethical reasoning might work
* these depend a lot on human imitation stuff / staying in human language. so any ideas other than pretraining responsible for this also count. eg RL training with human trainers giving ideas