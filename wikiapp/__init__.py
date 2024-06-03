import importlib.metadata
import warnings

try:
    __version__ = importlib.metadata.version("wikiapp_rd")
except importlib.metadata.PackageNotFoundError as e:
    warnings.warn(f"Could not determine version of wikiapp_rd", stacklevel=1)
    warnings.warn(str(e), stacklevel=1)
    __version__ = "unknown"
