$body = @{
    status_checking   = 1.0
    duration          = 12.0
    credit_history    = 2.0
    purpose           = 0.0
    credit_amount     = 1000.0
    savings_account   = 1.0
    employment_since  = 2.0
    installment_rate  = 4.0
    personal_status   = 1.0
    other_debtors     = 0.0
    residence_since   = 3.0
    property          = 2.0
    age               = 25.0
    other_installment_plans = 0.0
    housing           = 1.0
    existing_credits  = 1.0
    job               = 2.0
    liable_people     = 1.0
    telephone         = 0.0
    foreign_worker    = 1.0
} | ConvertTo-Json -Depth 10

return $body # Important to return the value