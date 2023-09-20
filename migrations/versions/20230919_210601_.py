"""empty message

Revision ID: 2708870e8257
Revises: 
Create Date: 2023-09-19 21:06:01.046378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2708870e8257'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.Date(), nullable=True),
    sa.Column('customer_id', sa.String(length=50), nullable=True),
    sa.Column('policyNumber', sa.String(length=50), nullable=True),
    sa.Column('referralId', sa.Integer(), nullable=True),
    sa.Column('accountCreateDate', sa.DateTime(), nullable=True),
    sa.Column('igoDate', sa.DateTime(), nullable=True),
    sa.Column('offerDate', sa.DateTime(), nullable=True),
    sa.Column('applicationSignedDate', sa.DateTime(), nullable=True),
    sa.Column('issuedDate', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('paidToDate', sa.DateTime(), nullable=True),
    sa.Column('pending_ir', sa.Integer(), nullable=True),
    sa.Column('canceled_ir', sa.Integer(), nullable=True),
    sa.Column('declined_ir', sa.Integer(), nullable=True),
    sa.Column('monthlyPremium', sa.Float(), nullable=True),
    sa.Column('faceAmount', sa.Integer(), nullable=True),
    sa.Column('term', sa.Integer(), nullable=True),
    sa.Column('finalRateClass', sa.Integer(), nullable=True),
    sa.Column('finalRateClassName', sa.String(length=50), nullable=True),
    sa.Column('paidSource', sa.String(length=50), nullable=True),
    sa.Column('paidSource_campaign', sa.String(length=50), nullable=True),
    sa.Column('telesalesAgency', sa.String(length=50), nullable=True),
    sa.Column('agentName', sa.String(length=50), nullable=True),
    sa.Column('product', sa.String(length=50), nullable=True),
    sa.Column('initialProductType', sa.String(length=50), nullable=True),
    sa.Column('firstName', sa.String(length=50), nullable=True),
    sa.Column('lastName', sa.String(length=50), nullable=True),
    sa.Column('dateOfBirth', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('phoneNumber', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lastupdates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('updates')
    op.drop_table('records')
    # ### end Alembic commands ###
