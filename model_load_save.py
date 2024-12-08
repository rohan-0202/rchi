import os

import torch


def save_model(model: torch.nn.Module, path: str) -> None:
    """
    Save a PyTorch model state.

    Args:
        model: The PyTorch model to save
        path: Path where to save the model
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save the model state
    torch.save(model.state_dict(), path)
    print(f"Model saved successfully at: {path}")


def load_model(
    model: torch.nn.Module,
    path: str,
    device: str = "cuda" if torch.cuda.is_available() else "cpu",
) -> None:
    """
    Load a PyTorch model state.

    Args:
        model: The PyTorch model to load weights into
        path: Path to the model file
        device: Device to load the model onto ('cuda' or 'cpu')
    """
    if not os.path.exists(path):
        print(f"No model found at: {path}")
        return
    # Load model state
    state_dict = torch.load(path, map_location=device)
    model.load_state_dict(state_dict)
    model.to(device)
    print(f"Model loaded successfully from: {path}")


# Usage example:
if __name__ == "__main__":
    # Example model
    model = torch.nn.Linear(10, 2)

    # Save model
    save_model(model=model, path="models/model.pt")

    # Load model
    load_model(model=model, path="models/model.pt")
