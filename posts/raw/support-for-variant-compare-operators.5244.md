Leith | 2019-06-22 12:48:26 UTC | #1

So far we can compare for equality / inquality of variants, given that their types match.
But we can certainly do better?

Today I started implementing a compare operator involving two variants - I offer to return the resulting compare method(s) for inclusion in the variant class itself, rather than outside it as I am being forced to do.

I don't care if A is a float and B is an integer, I should still be able to compare them and tell which is greater or less or if they are the same.

Given that this kind of thinking won't work for a lot of the possible cases in Variant, it seems like a win in terms of hey, it will run relatively fast.

1. Compares of most variant types won't be supported.
2. Compares of any number type will be deduced using doubles.
3. Compares of strings will fall back to the string compare operators.

-------------------------

Leith | 2019-06-22 13:25:50 UTC | #2

void Panic(){
    ; // man this sucks
}

Variant A(1);
Variant B(2);
if(A>B) Panic;

We can't

-------------------------

SirNate0 | 2019-06-24 06:21:51 UTC | #3

I understand your goal (and I at least think it's a good idea), but I don't get your second post. Are you saying the initial idea wouldn't work?

-------------------------

Leith | 2019-06-24 07:22:27 UTC | #4

I'm saying that the Variant class does not support the "GreaterThan" operator, or any others, except for "Equality" - and then only when the types match exactly, not in cases where the actual types can be mapped to matching types.

As an example of the limitations of the ONLY existing compare operator, I cannot compare a Bool with an Integer, even though we know that the true value of a Bool can only be 0 or 1.

The following is a partial implementation of a variant compare that attempts type mapping.
I stress these things: firstly, it is NOT COMPLETE, secondly, some types will NEVER be supported because they are totally incompatible, and thirdly, this implementation (currently) requires that we provide "type hints".

Comparing variants will never be case-complete nor bullet-proof, but we can definitely do better than not providing operators at all.

[code]
    BTNodeState VariableCompare::HandleStep(){

        Urho3D::Variant vA, vB;
                 double dA, dB;


        switch(SourceType_A){
            case ConditionalValueSource::Actor:
                vA=tree_->btContext_->blackboard_[NameOrValue_A];
                break;
            case ConditionalValueSource::World:
                vA=context_->GetGlobalVar(NameOrValue_A);
                break;
            case ConditionalValueSource::Constant:
                vA.FromString(ValueType_A,NameOrValue_A);
                break;
            default:
                URHO3D_LOGERROR("Unhandled SourceType A in VariableCompare");
                return NS_ERROR;
        }


        switch(SourceType_B){
            case ConditionalValueSource::Actor:
                vB=tree_->btContext_->blackboard_[NameOrValue_B];
                break;
            case ConditionalValueSource::World:
                vB=context_->GetGlobalVar(NameOrValue_B);
                break;
            case ConditionalValueSource::Constant:
                vB.FromString(ValueType_B,NameOrValue_B);
                break;
            default:
                URHO3D_LOGERROR("Unhandled SourceType B in VariableCompare");
                return NS_ERROR;
        }

        switch(this->conditionOperator_){
            case ConditionalOperator::COND_EQUAL:
            if(vA==vB)
                return NS_SUCCESS;
            else
                return NS_FAILURE;
            break;

            case COND_GREATER:
                double dA, dB;
                switch(ValueType_A){
                    case VAR_BOOL:
                        dA=static_cast<double>(vA.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dA=vA.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type A detected in VariableCompare node");
                        return NS_ERROR;
                }
                switch(ValueType_B){
                    case VAR_BOOL:
                        dB=static_cast<double>(vB.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dB=vB.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type B detected in VariableCompare node");
                        return NS_ERROR;
                }

                if(dA>dB)
                    return NS_SUCCESS;
                else
                    return NS_FAILURE;
                break;

            case (COND_GREATER | COND_EQUAL):
                switch(ValueType_A){
                    case VAR_BOOL:
                        dA=static_cast<double>(vA.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dA=vA.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type A detected in VariableCompare node");
                        return NS_ERROR;
                }
                switch(ValueType_B){
                    case VAR_BOOL:
                        dB=static_cast<double>(vB.GetBool());
                        break;
                    case VAR_FLOAT:
                    case VAR_INT:
                    case VAR_DOUBLE:
                    case VAR_INT64:
                        dB=vB.GetDouble();
                    default:
                        URHO3D_LOGERROR("Unhandled Variant Type B detected in VariableCompare node");
                        return NS_ERROR;
                }
                if(dA>=dB)
                    return NS_SUCCESS;
                else
                    return NS_FAILURE;
                break;

            default:
                URHO3D_LOGERROR("Unhandled Operator in VariableCompare");
                return NS_ERROR;
        }
    }

[/code]

-------------------------

