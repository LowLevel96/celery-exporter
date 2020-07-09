import prometheus_client

TASKS = prometheus_client.Counter(
    "celery_tasks_total",
    "Number of task events.",
    ["namespace", "name", "state", "queue"],
)
TASKS_RUNTIME = prometheus_client.Histogram(
    "celery_tasks_runtime_seconds", "Task runtime.", ["namespace", "name", "queue"]
)
LATENCY = prometheus_client.Histogram(
    "celery_tasks_latency_seconds",
    "Time between a task is received and started.",
    ["namespace"],
)
WORKERS = prometheus_client.Gauge(
    "celery_workers", "Number of alive workers", ["namespace"]
)

STRATEGY_METRIC_CHECKED_IN = prometheus_client.Counter(
    "strategy_checked_in",
    "Process Strategy Checked In",
    ['strategy']
)

STRATEGY_METRIC_INITIALIZED = prometheus_client.Counter(
    "strategy_initialized",
    "Process Strategy Initialized",
    ['strategy']
)

STRATEGY_METRIC_COMPLETED = prometheus_client.Counter(
    "strategy_completed",
    "Process Strategy Completed",
    ['strategy']
)

STRATEGY_METRIC_INVALID = prometheus_client.Counter(
    "strategy_invalid",
    "Process Strategy Invalid",
    ['strategy']
)

STRATEGY_METRIC_DO_NOTHING = prometheus_client.Counter(
    "strategy_do_nothing",
    "Process Strategy Do Nothing",
    ['strategy']
)

STRATEGY_METRIC_ERROR = prometheus_client.Counter(
    "strategy_error",
    "Process Strategy Error",
    ['strategy']
)
