from setuptools import setup, find_packages

setup(
    name="mental_health_eda",  # Package name
    version="0.1.0",  # Initial version
    description="Mental health EDA and prediction project",
    author="Your Name",  # Replace with your name
    packages=find_packages(where="src"),  # Finds all packages in src/
    package_dir={"": "src"},  # Root folder for packages
    install_requires=["pandas", "numpy", "matplotlib", "scikit-learn"],  # Dependencies
    python_requires=">=3.7",  # Minimum Python version
)
