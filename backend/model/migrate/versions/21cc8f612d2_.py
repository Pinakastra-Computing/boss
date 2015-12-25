"""Add PromoCode Index on customer_id

Revision ID: 21cc8f612d2
Revises: 1751dd2a255
Create Date: 2015-09-01 16:33:17.159614

"""

# revision identifiers, used by Alembic.
revision = '21cc8f612d2'
down_revision = '1751dd2a255'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_promo_code_customer_id'), 'promo_code', ['customer_id'], unique=False)
    op.drop_constraint('promo_code_ibfk_1', 'promo_code', type_='foreignkey')
    op.create_foreign_key(None, 'promo_code', 'customer', ['customer_id'], ['customer_id'], ondelete='CASCADE')
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'promo_code', type_='foreignkey')
    op.create_foreign_key('promo_code_ibfk_1', 'promo_code', 'customer', ['customer_id'], ['customer_id'])
    op.drop_index(op.f('ix_promo_code_customer_id'), table_name='promo_code')
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

