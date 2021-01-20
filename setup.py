from setuptools import find_packages, setup

setup(
    name="background_matting_v2",
    version="0.0.2",
    zip_safe=False,
    include_package_data=True,
    package_data={"background_matting_v2": ["py.typed"]},
    packages=find_packages(),
    install_requires=[
        "kornia==0.4.*",
        "tensorboard==2.3.*",
        "torch==1.7.*",
        "torchvision==0.8.*",
        "tqdm==4.51.*",
        "opencv-python==4.4.0.*",
        "onnxruntime==1.6.*",
    ],
)
