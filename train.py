import wandb

wandb.init(project="your-project-name")

for epoch in range(10):
    loss = model.train_step()
    wandb.log({"epoch": epoch, "loss": loss})
