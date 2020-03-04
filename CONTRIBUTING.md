# How to Contribute

Government employees, the public, and members of the private sector are encouraged to contribute to the repository by forking and submitting a pull request.

(If you are new to GitHub, you might start with a [basic tutorial](https://help.github.com/en/articles/set-up-git) and check out a more detailed guide to [pull requests](https://help.github.com/articles/using-pull-requests/).)

Pull requests will be evaluated by the repository guardians on a schedule and if deemed beneficial will be committed to the master branch.

All contributors retain the original copyright to their work, but by contributing to this project, you grant a world-wide, royalty-free, perpetual, irrevocable, non-exclusive, transferable license to all users under the terms of the license under which this project is distributed.

## Adding Frontend and Backend Boosters

All boosters must be contained in public GitHub repositories. They must also meet the following requirements.
- Must contain a `Dockerfile` in the project root directory
- A backend booster must expose its API on port 5000
- A frontend booster must expose its web app on port 3000
- Backend boosters must abide by the [Swagger definition](https://editor.swagger.io/?url=https://raw.githubusercontent.com/bcgov/openshift-launchpad/BOIL-67-contribution-guidelines/swagger.yaml)

Once the above requirements have been met, you may request that the booster be added to the OpenShift Launchpad. This may be requested in the following ways.
- Open a pull request with the requisite changes made to the choose-your-own-adventure script
- Create a GitHub issue explaining the request and include the booster repository
