import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Importdados } from './importdados';

describe('Importdados', () => {
  let component: Importdados;
  let fixture: ComponentFixture<Importdados>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Importdados]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Importdados);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
