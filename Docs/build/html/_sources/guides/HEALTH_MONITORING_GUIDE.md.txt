# System Health Monitoring Guide

## Overview

The webapp-pwa-notifications system includes comprehensive health monitoring capabilities to track system performance, detect failures, and alert administrators to issues. This guide covers all monitoring, alerting, and troubleshooting features.

## Architecture

### Components

#### 1. SystemHealthMonitor
- **Purpose**: Performs system-wide health checks
- **Location**: `notifications/error_handlers.py`
- **Functionality**:
  - Database connectivity checks
  - Error rate calculation
  - Calendar service monitoring
  - Push notification service status

#### 2. SystemAlertingService
- **Purpose**: Creates and manages system alerts
- **Location**: `notifications/error_handlers.py`
- **Functionality**:
  - Alert creation with threshold-based triggering
  - Alert consolidation (prevents duplicates)
  - Alert resolution and history tracking
  - Severity-based alert management

#### 3. PerformanceMonitor
- **Purpose**: Collects comprehensive performance metrics
- **Location**: `notifications/services.py`
- **Functionality**:
  - Notification statistics collection
  - Push subscription tracking
  - Processing performance metrics
  - Error rate statistics
  - Delivery metrics by notification type
  - Trend analysis

#### 4. SystemAlert Model
- **Purpose**: Stores alert data for history and tracking
- **Location**: `notifications/models.py`
- **Fields**:
  - Alert type and severity
  - Description and component info
  - Metric and threshold values
  - Trigger count and timestamps
  - Resolution tracking

### Alert Types

The system supports the following alert types:

| Alert Type | Severity | Trigger Condition |
|-----------|----------|-------------------|
| `push_service_failure` | Critical | Push notifications failing to send |
| `high_error_rate` | Warning | Error rate exceeds 5% |
| `push_delivery_degradation` | Warning | Delivery rate below 80% |
| `database_error` | Critical | Database connectivity issues |
| `calendar_service_unavailable` | Warning | Calendar service down |
| `performance_degradation` | Warning | System performance metrics exceeded |
| `queue_buildup` | Warning | Notification queue > 1000 items |
| `subscription_expiration` | Info | Push subscriptions expiring |
| `cache_failure` | Warning | Cache system errors |
| `batch_processor_failure` | Critical | Batch processing errors |

### Thresholds

Default thresholds for alert triggering:

```python
THRESHOLDS = {
    'error_rate': 0.05,                  # 5% error rate
    'push_delivery_rate': 0.80,          # 80% minimum delivery rate
    'push_failure_rate': 0.10,           # 10% maximum failure rate
    'database_error_rate': 0.02,         # 2% database error rate
    'queue_size': 1000,                  # Maximum notifications in queue
    'calendar_errors_per_hour': 5,       # Calendar service errors
}
```

## API Endpoints

### Health Check Endpoint

**GET** `/api/admin/system-health/`

Requires: Staff authentication

Returns comprehensive system health status including:
- Component health (database, push service, batch processor, cache)
- Performance metrics
- Delivery metrics by type
- 7-day trend analysis
- Active alert summary

**Response Example:**

```json
{
  "status": "healthy",
  "timestamp": "2026-07-26T10:30:00Z",
  "overall_status": "healthy",
  "components": {
    "database": {
      "status": "healthy",
      "details": "Database responsive, 1234 notifications"
    },
    "push_service": {
      "status": "healthy",
      "details": "156 active push subscriptions"
    },
    "batch_processor": {
      "status": "healthy",
      "details": "Success rate: 98.5%"
    },
    "cache": {
      "status": "healthy",
      "details": "Cache system responsive"
    }
  },
  "performance_metrics": {
    "notification_stats": {
      "total_notifications": 5432,
      "notifications_last_hour": 45,
      "notifications_last_day": 234,
      "unread_notifications": 89,
      "read_rate": 0.84
    },
    "push_subscription_stats": {
      "total_subscriptions": 156,
      "active_subscriptions": 148,
      "activation_rate": 0.95
    },
    "processing_performance": {
      "push_delivery_rate": 0.92,
      "push_failure_rate": 0.08,
      "total_push_attempts_24h": 450
    },
    "error_rates": {
      "overall_error_rate": 0.04,
      "success_rate": 0.96
    }
  },
  "delivery_metrics_by_type": {
    "maintenance_reminder": {
      "total": 120,
      "sent": 115,
      "delivery_rate": 0.96,
      "read": 89,
      "read_rate": 0.74
    },
    "inspection_reminder": {
      "total": 85,
      "sent": 78,
      "delivery_rate": 0.92,
      "read": 62,
      "read_rate": 0.73
    }
  },
  "trend_analysis": {
    "period_days": 7,
    "daily_stats": [
      {
        "date": "2026-07-19",
        "total": 245,
        "sent": 238,
        "delivery_rate": 0.97,
        "read_rate": 0.82
      }
    ],
    "delivery_trend": "stable"
  },
  "active_alerts": [],
  "alert_summary": {
    "critical_alerts": 0,
    "warning_alerts": 0,
    "total_active": 0
  }
}
```

### System Alerts Endpoint

**GET** `/api/admin/system-alerts/`

Requires: Staff authentication

Query Parameters:
- `severity`: Filter by severity (critical, warning, info)
- `alert_type`: Filter by alert type
- `active_only`: Show only active alerts (default: true)

Returns list of system alerts with details.

**POST** `/api/admin/system-alerts/`

Requires: Staff authentication

Resolve an alert.

Request body:
```json
{
  "alert_id": 123,
  "resolution_notes": "Issue fixed by restarting service"
}
```

## Programmatic Usage

### Creating Alerts

```python
from notifications.error_handlers import SystemAlertingService

# Create a basic alert
alert = SystemAlertingService.create_alert(
    alert_type='high_error_rate',
    title='High Error Rate Detected',
    description='Error rate of 8% exceeds threshold of 5%',
    affected_component='Notification Processing',
    metric_value=0.08,
    threshold_value=0.05
)

# Create alert with metadata
alert = SystemAlertingService.create_alert(
    alert_type='push_delivery_degradation',
    title='Push Delivery Rate Degradation',
    description='Delivery rate of 75% below threshold of 80%',
    affected_component='Push Notification Service',
    metric_value=0.75,
    threshold_value=0.80,
    metadata={
        'notification_type': 'maintenance_reminder',
        'sample_size': 250
    }
)
```

### Checking and Alerting

```python
from notifications.error_handlers import SystemAlertingService

# Check error rate and alert if exceeded
error_rate = 0.08
SystemAlertingService.check_and_alert_error_rate(error_rate, '24hour')

# Check delivery rate and alert if below threshold
delivery_rate = 0.75
SystemAlertingService.check_and_alert_delivery_rate(delivery_rate, 'all')

# Check push failure rate
failure_rate = 0.12
SystemAlertingService.check_and_alert_push_failures(failure_rate)

# Check generic performance metric
SystemAlertingService.check_and_alert_performance(
    'average_processing_time_ms',
    metric_value=450,
    threshold=300
)
```

### Resolving Alerts

```python
from notifications.error_handlers import SystemAlertingService

# Resolve alerts by type
resolved_count = SystemAlertingService.resolve_alert(
    alert_type='high_error_rate',
    affected_component='Notification Processing',
    resolution_notes='Issue fixed by optimizing queries'
)

# Or resolve individual alert
from notifications.models import SystemAlert

alert = SystemAlert.objects.get(id=123)
alert.resolve('Issue has been resolved')
```

### Getting Active Alerts

```python
from notifications.error_handlers import SystemAlertingService

# Get all active alerts
alerts = SystemAlertingService.get_active_alerts()

# Get critical alerts only
critical_alerts = SystemAlertingService.get_active_alerts(severity='critical')

# Get specific alert type
delivery_alerts = SystemAlertingService.get_active_alerts(
    alert_type='push_delivery_degradation'
)
```

### Performance Metrics

```python
from notifications.services import PerformanceMonitor

monitor = PerformanceMonitor()

# Get comprehensive metrics
metrics = monitor.get_system_performance_metrics()

# Get delivery metrics by notification type
delivery_by_type = monitor.get_delivery_metrics_by_type()
# Returns:
# {
#   'maintenance_reminder': {
#     'total': 120,
#     'sent': 115,
#     'delivery_rate': 0.96,
#     'read': 89,
#     'read_rate': 0.74
#   },
#   'inspection_reminder': {...}
# }

# Get trend analysis
trends = monitor.get_trend_analysis(days=7)
# Returns daily stats and trend direction

# Check thresholds and create alerts
monitor.check_performance_thresholds()
```

## Monitoring Dashboard

### Key Metrics to Monitor

1. **System Health Status**
   - Overall health: healthy, degraded, unhealthy
   - Component statuses
   - Active alert count

2. **Notification Metrics**
   - Total notifications created
   - Read rate
   - Unread count
   - Notification distribution by type

3. **Push Notification Metrics**
   - Active subscriptions
   - Delivery rate
   - Failure rate
   - Trend analysis

4. **Performance Metrics**
   - Error rates
   - Processing times
   - Database performance
   - Cache effectiveness

### Dashboard Access

Staff members can access the health monitoring dashboard at:
- `GET /api/admin/system-health/` - Full health status
- `GET /api/admin/system-alerts/` - Active alerts
- `GET /api/admin/performance-metrics/` - Performance data

## Troubleshooting

### High Error Rate Alert

**Cause**: Push notification failures exceeding 5% threshold

**Investigation**:
1. Check push subscription validity
2. Verify VAPID keys are configured correctly
3. Check for database connectivity issues
4. Review notification retry history

**Resolution**:
1. Remove invalid subscriptions
2. Restart push notification service
3. Check and optimize database queries
4. Monitor for patterns in failures

### Push Delivery Degradation Alert

**Cause**: Successful delivery rate below 80%

**Investigation**:
1. Analyze failed delivery logs
2. Check subscription expiration dates
3. Review network connectivity
4. Check service worker registration

**Resolution**:
1. Clean up expired subscriptions
2. Investigate failed delivery reasons
3. Check client-side service worker health
4. Monitor delivery rates over time

### Database Error Alert

**Cause**: Database connectivity or performance issues

**Investigation**:
1. Check database connection status
2. Monitor database query performance
3. Check for connection pool exhaustion
4. Review slow query logs

**Resolution**:
1. Restart database service if needed
2. Optimize slow queries
3. Increase connection pool size
4. Check disk space and memory

### Calendar Service Unavailable

**Cause**: Calendar service not responding

**Investigation**:
1. Verify calendar service is running
2. Check network connectivity
3. Review service logs
4. Check service configuration

**Resolution**:
1. Restart calendar service
2. Verify service configuration
3. Check network connectivity
4. Review and fix service issues

## Alerting Strategies

### Critical Alerts
Should trigger immediate notification to on-call staff:
- Push service failures
- Database errors
- Batch processor failures

### Warning Alerts
Should be reviewed during regular monitoring:
- High error rates
- Delivery rate degradation
- Performance issues
- Calendar service problems

### Info Alerts
Can be archived after review:
- Subscription expirations
- Minor performance variations
- Non-critical service issues

## Performance Optimization Based on Alerts

### When Error Rate is High
1. Check for invalid notification data
2. Optimize error handling
3. Review retry mechanisms
4. Analyze failed notification patterns

### When Delivery Rate is Low
1. Check subscription health
2. Verify VAPID configuration
3. Monitor network connectivity
4. Review push service logs

### When Processing Performance Degrades
1. Check database query performance
2. Optimize batch processing
3. Review cache effectiveness
4. Monitor resource utilization

## Integration with External Monitoring

### Prometheus Metrics

The system can expose metrics to Prometheus:
- Notification counts
- Delivery rates
- Error rates
- Processing times
- Active subscriptions

### Alerting Integration

Alerts can be integrated with external alerting systems:
- Webhook notifications
- Email alerts
- Slack integration
- PagerDuty integration

## Best Practices

1. **Regular Monitoring**: Check health status and alerts daily
2. **Alert Resolution**: Resolve alerts promptly with notes
3. **Trend Analysis**: Review trends weekly to identify patterns
4. **Threshold Adjustment**: Update thresholds based on actual performance
5. **Documentation**: Document all alert resolutions for future reference
6. **Alert Fatigue**: Review and adjust thresholds to reduce false positives
7. **Performance Baseline**: Establish baseline metrics for comparison
8. **Root Cause Analysis**: Investigate underlying causes, not just symptoms

## Management Commands

### Health Check Command

```bash
python manage.py manage_notification_system health-check
```

Performs comprehensive system health check with output.

### Check System Health Programmatically

```python
from notifications.error_handlers import SystemHealthMonitor

health_status = SystemHealthMonitor.check_notification_system_health()
print(f"System Health: {health_status['status']}")
if health_status['issues']:
    for issue in health_status['issues']:
        print(f"Issue: {issue}")
```

## Summary

The health monitoring system provides comprehensive visibility into notification system health and performance. Regular monitoring and prompt alert resolution ensure optimal system reliability and user experience.
