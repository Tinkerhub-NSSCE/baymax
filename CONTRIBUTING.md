![baymax](https://user-images.githubusercontent.com/78845005/194762101-93950c17-0b1b-4f60-8426-b35a2b57fb84.png)

# Contributing to Baymax

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs-)
  - [Suggesting Enhancements](#suggesting-enhancements-)
  - [Your First Code Contribution](#your-first-code-contribution-)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)


## Code of Conduct

This project and everyone participating in it is governed by our
[Code of Conduct](https://github.com/Tinkerhub-NSSCE/baymax/blob/master/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to <tinkerhubnnssce@gmail.com>.


## I Have a Question

Before you ask a question, it is best to search for existing [Issues](https://github.com/Tinkerhub-NSSCE/baymax//issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/Tinkerhub-NSSCE/baymax//issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (python, discord.py, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Reporting Bugs 🐛

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/Tinkerhub-NSSCE/baymax/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <tinkerhubnnssce@gmail.com>.
<!-- You may add a PGP key to allow the messages to be sent encrypted as well. -->

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/Tinkerhub-NSSCE/baymax//issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).


### Suggesting Enhancements ✨

This section guides you through submitting an enhancement suggestion for Baymax, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](#) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/Tinkerhub-NSSCE/baymax//issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/Tinkerhub-NSSCE/baymax//issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. <!-- this should only be included if the project has a GUI -->
- **Explain why this enhancement would be useful** to most Baymax users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

### Your First Code Contribution 💡

#### Local Configuration
You can host the bot locally by configuring all necessary values in the `config.ini` file

- Copy `config.ini.sample` to a new file `config.ini` and replace all placeholders with appropriate values
- Copy `.env.sample` to a new file `.env` and replace the placeholder with your bot token
- Download a private key file for dialogflow in json format from your google cloud console. To learn more click [here](https://cloud.google.com/dialogflow/es/docs/quick/setup)
- Rename the downloaded file to `dialogflow_api.json` and place it in the root directory
- Install all the requirements
```bash
$ pip install -r requirements.txt
```
- Run the bot
```bash
$ python main.py
```

#### How do I get started?
A few beginner friendly issues have already been opened in our [issue tracker](https://github.com/Tinkerhub-NSSCE/baymax//issues). You can get started with any of them if you'd like to. Here are a few resources you might find useful to start contributing.

- [discordpy](https://discordpy.readthedocs.io/en/stable/)
- [dialogflow](https://cloud.google.com/dialogflow/es/docs)
- [google-cloud-dialogflow](https://googleapis.dev/python/dialogflow/latest/index.html)
- [pyairtable](https://pyairtable.readthedocs.io/en/latest/)
- [pillow](https://pillow.readthedocs.io/en/stable/)

## Styleguides
### Commit Messages
Normal meaningful and simple commit messages are always welcome. If you like to follow any standards you can check this out 👉 [Conventional Commits](https://www.conventionalcommits.org/) - a specification for adding human and machine readable meaning to commit messages.

