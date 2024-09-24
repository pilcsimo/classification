import torch
import torch.nn as nn

from .utils import load_module

def test_assignment_3_1(
    src_dir: str, verification_file: str, seed: int = 69, generate: bool = False
) -> dict:

    lin_classifier_module = load_module(src_dir, "linear_classifier")
    LinearClassifier = lin_classifier_module.LinearClassifier

    ret = {"points": 0, "message": "", "max_points": 1}

    num_classes = 10
    num_features = 5
    num_samples = 100

    torch.random.manual_seed(seed)

    params = dict(
        W=nn.Parameter(torch.randn(num_features, num_classes, dtype=torch.float)),
        b=nn.Parameter(torch.randn(num_classes, dtype=torch.float)),
    )
    X = torch.randn(num_samples, num_features)

    try:
        model = LinearClassifier(num_classes, num_features)
        model.params = params
        logits = model.forward(X)
    except Exception as e:
        ret["message"] = f"\tFAILED! \n\t{e}"
        return ret

    if generate:
        torch.save(logits, verification_file)
        print(f"Successfully generated '{verification_file}'!")
    else:
        expected_logits = torch.load(verification_file, weights_only=True)

        try:
            if torch.allclose(logits, expected_logits):
                ret["message"] = f"PASSED!"
                ret["points"] = ret["max_points"]
            else:
                difference = torch.sum(torch.abs(logits - expected_logits))
                ret["message"] = f"\tFAILED! \n\tDifference of logits: {difference}"
        except Exception as e:
            ret["message"] = f"\tFAILED! \n\t{e}"

    return ret


def test_assignment_3_2(
    src_dir: str, verification_file: str, seed: int = 69, generate: bool = False
) -> dict:

    lin_classifier_module = load_module(src_dir, "linear_classifier")
    LinearClassifier = lin_classifier_module.LinearClassifier

    ret = {"points": 0, "message": "", "max_points": 1}

    num_classes = 10
    num_features = 5
    num_samples = 100

    torch.random.manual_seed(seed)

    params = dict(
        W=nn.Parameter(torch.randn(num_features, num_classes, dtype=torch.float)),
        b=nn.Parameter(torch.randn(num_classes, dtype=torch.float)),
    )
    X = torch.randn(num_samples, num_features)

    try:
        model = LinearClassifier(num_classes, num_features)
        model.params = params
        y_pred = model.predict(X)
    except Exception as e:
        ret["message"] = f"\tFAILED! \n\t{e}"
        return ret

    if generate:
        torch.save(y_pred, verification_file)
        print(f"Successfully generated '{verification_file}'!")
    else:
        expected_logits = torch.load(verification_file, weights_only=True)

        try:
            if torch.allclose(y_pred, expected_logits):
                ret["message"] = f"PASSED!"
                ret["points"] = ret["max_points"]
            else:
                difference = torch.sum(torch.abs(y_pred - expected_logits))
                ret[
                    "message"
                ] = f"\tFAILED! \n\tDifference of predicted labels: {difference}"
        except Exception as e:
            ret["message"] = f"\tFAILED! \n\t{e}"

    return ret


def test_assignment_3_3(
    src_dir: str, verification_file: str, seed: int = 69, generate: bool = False
) -> dict:

    lin_classifier_module = load_module(src_dir, "linear_classifier")
    LinearClassifier = lin_classifier_module.LinearClassifier

    ret = {"points": 0, "message": "", "max_points": 1}

    num_classes = 10
    num_features = 5
    num_samples = 100

    torch.random.manual_seed(seed)

    params = dict(
        W=nn.Parameter(torch.randn(num_features, num_classes, dtype=torch.float)),
        b=nn.Parameter(torch.randn(num_classes, dtype=torch.float)),
    )
    X = torch.randn(num_samples, num_features)
    y = torch.randint(0, num_classes, (num_samples,))

    try:
        model = LinearClassifier(num_classes, num_features)
        model.params = params
        loss = model.loss(X, y)
    except Exception as e:
        ret["message"] = f"\tFAILED! \n\t{e}"
        return ret

    if generate:
        torch.save(loss, verification_file)
        print(f"Successfully generated '{verification_file}'!")
    else:
        expected_loss = torch.load(verification_file, weights_only=True)

        try:
            if torch.allclose(loss, expected_loss):
                ret["message"] = f"PASSED!"
                ret["points"] = ret["max_points"]
            else:
                difference = torch.sum(torch.abs(loss - expected_loss))
                ret["message"] = f"\tFAILED! \n\tLoss difference: {difference}"
        except Exception as e:
            ret["message"] = f"\tFAILED! \n\t{e}"

    return ret


def test_assignment_3_4(
    src_dir: str, verification_file: str, seed: int = 69, generate: bool = False
) -> dict:

    lin_classifier_module = load_module(src_dir, "linear_classifier")
    LinearClassifier = lin_classifier_module.LinearClassifier

    ret = {"points": 0, "message": "", "max_points": 1}

    num_classes = 10
    num_features = 5
    num_samples = 100

    torch.random.manual_seed(seed)

    params = dict(
        W=nn.Parameter(torch.randn(num_features, num_classes, dtype=torch.float)),
        b=nn.Parameter(torch.randn(num_classes, dtype=torch.float)),
    )
    X = torch.randn(num_samples, num_features)
    y = torch.randint(0, num_classes, (num_samples,))

    try:
        model = LinearClassifier(num_classes, num_features)
        model.params = params
        model._zero_gradients()
        loss = model.loss(X, y)
        loss.backward(retain_graph=True)
        model._update_weights()

    except Exception as e:
        ret["message"] = f"\tFAILED! \n\t{e}"
        return ret

    if generate:
        torch.save(model.params, verification_file)
        print(f"Successfully generated '{verification_file}'!")
    else:
        expected_params = torch.load(verification_file, weights_only=True)

        try:
            pred_values = model.params.values()
            expected_values = expected_params.values()
            differences = [
                torch.sum(torch.abs(m - exp_m))
                for m, exp_m in zip(pred_values, expected_values)
            ]
            differences = torch.stack(differences)
            param_difference = torch.sum(differences)

            if param_difference < 1e-5:
                ret["message"] = f"PASSED!"
                ret["points"] = ret["max_points"]
            else:
                ret[
                    "message"
                ] = f"\tFAILED! \n\tParameter difference: {param_difference}"
        except Exception as e:
            ret["message"] = f"\tFAILED! \n\t{e}"

    return ret
