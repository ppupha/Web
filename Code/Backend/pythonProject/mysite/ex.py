from unittest import TestCase, mock


class Task:

    def action(self):
        return "FOO BAR"


@mock.patch("__main__.Task")
def mock_task_class(mock_class):
    print(mock_class)  # Will print MagicMock instance
    mock_class.return_value.action.return_value = "FOO ONLY"
    task_instance = Task()
    print(task_instance.action())  # Will print "FOO ONLY"

mock_task_class()