import wandb

wandb.init(project="your-project-name")

accuracy = model.evaluate()
wandb.log({"accuracy": accuracy})
